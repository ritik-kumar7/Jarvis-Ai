from utils.brain import JarvisBrain
from utils.memory import ConversationMemory
import threading

class Jarvis:
    def __init__(self):
        self.brain = JarvisBrain()
        self.memory = ConversationMemory()
        self.lock = threading.Lock()
    
    def respond(self, user_input: str) -> str:
        with self.lock:
            context = self.memory.get_context()
            response = self.brain.solve(user_input, context)
            self.memory.store_interaction(user_input, response)
            return response

if __name__ == "__main__":
    jarvis = Jarvis()
    print("Jarvis initialized. How can I help? (Type 'exit' to quit)")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                break
                
            response = jarvis.respond(user_input)
            print("Jarvis:", response)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print("Error:", str(e))