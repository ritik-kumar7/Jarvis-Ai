import re

class ProblemClassifier:
    def __init__(self):
        self.problem_types = {
            'math': [
                'calculate', 'solve', 'evaluate', 'simplify', 'find the value of', 
                '+', '-', '*', '/', '^', 'integral', 'derivative', 'limit', 'equation', 
                'factor', 'root', 'algebra', 'geometry', 'probability', 'calculus', 'math problem'
            ],
            'code': [
                'write code','write a python code','write a code', 'code for', 'program that', 'function that', 'algorithm for',
                'python program', 'implement', 'logic for', 'debug', 'optimize', 'write a script', 
                'programming task', 'build a program', 'code example', 'function in python','write a program ','write a code of'
            ],
            'general_knowledge': [
                'what is', 'who is', 'define', 'explain', 'tell me about', 'how does', 
                'history of', 'capital of', 'founder of', 'meaning of', 'when did', 'why is', 
                'what happened', 'who invented', 'where is', 'how do', 'who discovered',
                'what are', 'who are', 'where was', 'when was', 'how was',
                'name of', 'purpose of', 'role of', 'importance of', 'origin of',
                'advantages of', 'disadvantages of', 'difference between', 'types of',
                'uses of', 'examples of', 'summary of', 'impact of', 'effect of',
                'contribution of', 'function of', 'application of', 'features of',
                'benefits of', 'explanation of', 'overview of', 'laws of', 'principle of',
                'science behind', 'formula of', 'structure of'
            ],
            'task_automation': [
                'remind me', 'set timer', 'schedule', 'create reminder', 'alert me', 
                'alarm', 'task reminder', 'set an alarm', 'send a reminder', 'remind me to'
            ],
            'creative': [
                'write a poem', 'poem about', 'story about', 'lyrics for', 'compose a song', 
                'creative writing', 'write a joke', 'create a story', 'generate poem', 
                'creative idea', 'write a letter', 'make a short story', 'write a fictional story'
            ],
            'analysis': [
                'analyze', 'analysis of', 'compare', 'statistics', 'trends in', 'pattern in', 
                'insights from', 'data of', 'breakdown of', 'overview of', 'summary of', 'evaluate the data'
            ],
            'self_intro': [
                'what is your name', 'who are you', 'introduce yourself', 'tell me about you', 
                'who created you', 'how do you work', 'what can you do', 'what are you capable of', 
                'why are you called', 'where do you live', 'how old are you', 'what is your purpose', 
                'do you have a name', 'who built you', 'who trained you', 'what is your story', 
                'how do you operate', 'are you real', 'can you think', 'are you intelligent', 'do you sleep',
                'hello', 'hi', 'hey', 'hey there', 'hi there', 'good morning', 'good afternoon', 'good evening',
                'how are you', 'how’s it going', 'what’s up', 'how do you do', 'yo', 'wassup','what is your name'
            ],
            'joke': [
                'tell me a joke', 'make me laugh', 'tell me something funny', 'tell me a funny story', 
                'joke for me', 'funny joke', 'say something funny', 'give me a joke', 'crack a joke','another joke','next joke'
            ],

            'general_question': [
                'how have you been', 'how’s everything', 'what’s going on', 'yo', 'what’s new', 
                'how’s life', 'tell me something interesting', 'anything new', 'what is happening'
            ]
            

            


        }

    def classify(self, query: str) -> str:
        query = query.lower().strip()
        query = re.sub(r'[^\w\s]', '', query)  # Remove punctuation

        for p_type, keywords in self.problem_types.items():
            if any(re.search(r'\b' + re.escape(kw) + r'\b', query) for kw in keywords):  # Whole word matching
                return p_type

        return 'general_conversation'

