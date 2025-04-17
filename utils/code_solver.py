import re
from typing import Dict, Optional
from .base_solver import BaseSolver
from .code_data import CODE_SOLUTIONS

class CodeSolver(BaseSolver):
    def __init__(self):
        super().__init__()
        self.language_map = {
            'python': 'python',
            'java': 'java',
            'cpp': 'cpp',
            'javascript': 'javascript',
            'go': 'go',
            'c': 'c'
        }

    def handle(self, query: str, context: str = "") -> str:
        """Handle code generation requests from the code database"""
        try:
            lang = self.detect_language(query)
            normalized_query = self._normalize_query(query)

            if lang in CODE_SOLUTIONS:
                solution = self._find_best_matching_solution(normalized_query, CODE_SOLUTIONS[lang])
                if solution:
                    return self._format_code(solution["code"], lang)

            return "I'm still learning how to handle that. Could you provide more details?"

        except Exception as e:
            return f"⚠️ Error processing code request: {str(e)}"

    def detect_language(self, query: str) -> str:
        """Detect programming language from query"""
        query = query.lower()
        for lang in self.language_map:
            if lang in query:
                return self.language_map[lang]
        return 'python'  # default

    def _normalize_query(self, query: str) -> str:
        """Normalize the query for better matching"""
        query = query.lower()
        query = re.sub(
            r'(write|create|make|how to|function to|program to|code for|'
            r'python function|python code|python program|implement|build|generate)\s+',
            '', query)
        query = re.sub(r'[^\w\s]', '', query)  # Remove punctuation
        query = re.sub(r'\s+', ' ', query).strip()
        return query

    def _find_best_matching_solution(self, query: str, solutions: list) -> Optional[Dict]:
        """Find the best matching solution based on prompt similarity"""
        best_score = 0
        best_solution = None

        for solution in solutions:
            for prompt in solution["prompts"]:
                score = self._matching_score(query, prompt)
                if score > best_score:
                    best_score = score
                    best_solution = solution

        return best_solution if best_score >= 0.5 else None  # adjust threshold as needed

    def _matching_score(self, query: str, prompt: str) -> float:
        """Calculate a score based on word overlap"""
        query_words = set(self._normalize_query(query).split())
        prompt_words = set(self._normalize_query(prompt).split())
        if not prompt_words:
            return 0.0

        common = query_words & prompt_words
        essential_keywords = {'check', 'find', 'print', 'number', 'string', 'list', 'palindrome', 'even', 'odd', 'reverse', 'sum', 'factorial'}

        # Boost score if essential keywords are shared
        essential_overlap = common & essential_keywords
        keyword_bonus = 0.2 if len(essential_overlap) >= 2 else 0.0

        return (len(common) / len(prompt_words)) + keyword_bonus

    def _format_code(self, code: str, lang: str) -> str:
        """Format the code output with proper markdown"""
        return f"```{lang}\n{code}\n```"
