from .base_solver import BaseSolver
import random

class DefaultResponder(BaseSolver):
    def __init__(self):
        self.responses = [
            "I'm not sure I understand. Could you rephrase?",
            "That's an interesting request. Let me think...",
            "I'm still learning how to handle that.",
            "Could you provide more details?",
            "I might need more context to help."
        ]
    
    def handle(self, query: str, context: str = "") -> str:
        return random.choice(self.responses)