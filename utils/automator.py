import os
import re
import time
from threading import Timer
import datetime
from .base_solver import BaseSolver
from utils.brain import BaseSolver

class TaskAutomator(BaseSolver):
    def __init__(self):
        self.active_timers = {}
    
    def handle(self, query: str, context: str = "") -> str:
        try:
            query = query.lower()
            
            if any(cmd in query for cmd in ['remind me', 'set reminder']):
                return self._set_reminder(query)
            elif 'timer' in query:
                return self._set_timer(query)
            elif any(cmd in query for cmd in ['note', 'make a note']):
                return self._take_note(query)
            return "I can set reminders, timers, or take notes."
        except Exception as e:
            return f"Task error: {str(e)}"
    
    def _set_reminder(self, query: str) -> str:
        try:
            time_str = re.search(r'in (\d+) (minute|hour|second)', query)
            if not time_str:
                return "Please specify time like 'remind me in 5 minutes'"
            
            num, unit = time_str.groups()
            num = int(num)
            
            if unit == 'minute':
                delay = num * 60
            elif unit == 'hour':
                delay = num * 3600
            else:
                delay = num
                
            reminder = query.split('to')[-1].split('in')[0].strip()
            
            Timer(delay, self._alert, args=[reminder]).start()
            return f"Reminder set for {num} {unit}s: '{reminder}'"
        except Exception as e:
            return f"Couldn't set reminder: {str(e)}"
    
    def _set_timer(self, query: str) -> str:
        try:
            duration = re.search(r'(\d+) (minute|second|hour)', query)
            if not duration:
                return "Please specify duration like 'set timer for 5 minutes'"
            
            num, unit = duration.groups()
            num = int(num)
            
            if unit == 'minute':
                secs = num * 60
            elif unit == 'hour':
                secs = num * 3600
            else:
                secs = num
                
            Timer(secs, self._alert, args=["Timer completed!"]).start()
            return f"Timer set for {num} {unit}s"
        except Exception as e:
            return f"Couldn't set timer: {str(e)}"
    
    def _take_note(self, query: str) -> str:
        note = query.replace('note', '').replace('take a', '').strip()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        with open("notes.txt", "a") as f:
            f.write(f"[{timestamp}] {note}\n")
        
        return f"Note saved: '{note}'"
    
    def _alert(self, message: str):
        print(f"\nALERT: {message}\n")
        # On Windows
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 1000)