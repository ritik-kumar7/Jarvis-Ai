# utils/brain.py
from enum import Enum
from typing import Dict, Type
from .base_solver import BaseSolver
from .math_solver import MathSolver
from .code_solver import CodeSolver
from .knowledge_engine import KnowledgeEngine
from .automator import TaskAutomator
from .creative import CreativeWriter
from .analyzer import DataAnalyzer
from .default import DefaultResponder
from .self_intro_solver import SelfIntroSolver
from .joke_solver import JokeSolver 
class ProblemType(Enum):
    MATH = "math"
    CODE = "code"
    KNOWLEDGE = "knowledge"
    TASK = "task"
    CREATIVE = "creative"
    ANALYSIS = "analysis"
    UNKNOWN = "general"
    SELF_INTRO = "self_intro"
    JOKE  = "joke" 

class JarvisBrain:
    def __init__(self):
        self.solvers = self._initialize_solvers()
        
    def _initialize_solvers(self) -> Dict[ProblemType, BaseSolver]:
        return {
            ProblemType.MATH: MathSolver(),
            ProblemType.CODE: CodeSolver(),
            ProblemType.KNOWLEDGE: KnowledgeEngine(),
            ProblemType.TASK: TaskAutomator(),
            ProblemType.CREATIVE: CreativeWriter(),
            ProblemType.ANALYSIS: DataAnalyzer(),
            ProblemType.SELF_INTRO: SelfIntroSolver(),
            ProblemType.JOKE: JokeSolver(),   
            ProblemType.UNKNOWN: DefaultResponder()
            
        }
    
    def classify_problem(self, query: str) -> ProblemType:
        query = query.lower()
        
        classification_rules = {
            ProblemType.MATH: [
                'calculate', 'solve', 'evaluate', 'simplify', 'find the value of', 
                '+', '-', '*', '/', '^', 'integral', 'derivative', 'limit', 'equation', 
                'factor', 'root', 'algebra', 'geometry', 'probability', 'calculus', 'math problem', 
                'compute', 'work out', 'math question', 'what is the result of', 'find'
            ],
            ProblemType.CODE: [
                'write code', 'write a python code','write a code','code for', 'program that', 'function that', 'algorithm for',
                'python program', 'implement', 'logic for', 'debug', 'optimize', 'write a script', 
                'programming task', 'build a program', 'code example', 'function in python', 'fix', 
                'write a solution', 'build a function', 'how to implement', 'program a solution','write a program ','write a code of'
            ],
            ProblemType.KNOWLEDGE: [
                'what is', 'who is', 'define', 'explain', 'tell me about', 'how does', 
                'history of', 'capital of', 'founder of', 'meaning of', 'when did', 'why is', 
                'what happened', 'who invented', 'where is', 'how do', 'who discovered', 'what happened',
                'why does', 'tell me the story of', 'tell me the details of', 'give me information about'
            ],
            ProblemType.TASK: [
                'remind me', 'set timer', 'schedule', 'create reminder', 'alert me', 
                'alarm', 'task reminder', 'set an alarm', 'send a reminder', 'remind me to', 
                'schedule a meeting', 'make a note', 'set an appointment', 'create task', 'send me a reminder'
            ],
            ProblemType.CREATIVE: [
                'write a poem', 'poem about', 'story about', 'lyrics for', 'compose a song', 
                'creative writing', 'write a joke', 'create a story', 'generate poem', 
                'creative idea', 'write a letter', 'make a short story', 'write a fictional story', 
                'imagine a story', 'create a new song', 'compose a creative work', 'tell a joke', 
                'describe a situation', 'write an essay', 'make a play'
            ],
            ProblemType.ANALYSIS: [
                'analyze', 'analysis of', 'compare', 'statistics', 'trends in', 'pattern in', 
                'insights from', 'data of', 'breakdown of', 'overview of', 'summary of', 'evaluate the data',
                'study the results', 'interpret the data', 'compare the data', 'what does the data show', 
                'how does the data look', 'provide analysis for', 'data trends'
            ],
            ProblemType.SELF_INTRO: [
                'what is your name', 'who are you', 'introduce yourself', 'tell me about you', 
                'who created you', 'how do you work', 'what can you do', 'what are you capable of', 
                'why are you called', 'where do you live', 'how old are you', 'what is your purpose', 
                'do you have a name', 'who built you', 'who trained you', 'what is your story', 
                'how do you operate', 'are you real', 'can you think', 'are you intelligent', 'do you sleep',
                'hello', 'hi', 'hey', 'hey there', 'hi there', 'good morning', 'good afternoon', 'good evening',
                'how are you', 'how’s it going', 'what’s up', 'how do you do', 'yo', 'wassup', 
                'tell me about yourself', 'what makes you unique', 'do you have a personality','what is your name'
            ],
            ProblemType.JOKE: [
                'tell me a joke', 'joke', 'make me laugh', 'tell a joke', 'can you tell me a joke',
                'give me a joke', 'funny joke', 'tell me something funny','another joke','next joke'
            ]
        }
        
        for p_type, keywords in classification_rules.items():
            if any(kw in query for kw in keywords):
                return p_type
                
        return ProblemType.UNKNOWN
    
    def solve(self, query: str, context: str = "") -> str:
        problem_type = self.classify_problem(query)
        solver = self.solvers.get(problem_type, self.solvers[ProblemType.UNKNOWN])
        return solver.handle(query, context)
