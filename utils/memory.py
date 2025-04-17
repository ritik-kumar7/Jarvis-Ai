from collections import deque

class ConversationMemory:
    def __init__(self, max_length=5):
        self.history = deque(maxlen=max_length)
    
    def store_interaction(self, query: str, response: str):
        self.history.append((query, response))
    
    def get_context(self) -> str:
        return "\n".join(f"User: {q}\nJarvis: {r}" for q,r in self.history)
    
    def clear(self):
        self.history.clear()