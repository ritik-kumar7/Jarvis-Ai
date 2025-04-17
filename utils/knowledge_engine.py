from .base_solver import BaseSolver
import wikipedia
from transformers import pipeline
import re
import string


class KnowledgeEngine(BaseSolver):
    def __init__(self):
        self.qa_pipeline = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2"
        )
        self.cache = {}
        self.max_summary_length = 3  # Number of sentences from Wikipedia
        
        self.general_knowledge_keywords = [
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
        ]
    
    def handle(self, query: str, context: str = "") -> str:
        try:
            clean_query = self._clean_query(query)
            
            if self._is_general_knowledge_query(query):
                return self._get_wikipedia_answer(clean_query)
            
            return self._answer_with_qa(clean_query, context)
        except wikipedia.DisambiguationError as e:
            try:
                fallback = wikipedia.summary(e.options[0], sentences=self.max_summary_length)
                return fallback
            except Exception:
                return f"Multiple matches found. Please be more specific. Options: {', '.join(e.options[:3])}..."
        except wikipedia.PageError:
            return self._answer_with_qa(query, context)
        except Exception as e:
            return f"⚠️ Knowledge error: {str(e)}"
    
    def _clean_query(self, query: str) -> str:
        """Remove question words and punctuation"""
        query = query.lower()
        replacements = {
            r'what (is|are)\s+': '',
            r'who (is|are)\s+': '',
            r'explain\s+': '',
            r'tell me about\s+': '',
            r'^can you\s+': '',
            r'define\s+': '',
            r'please\s+': '',
            r'could you\s+': ''
        }
        for pattern, repl in replacements.items():
            query = re.sub(pattern, repl, query)
        
        query = query.translate(str.maketrans('', '', string.punctuation))
        return query.strip()

    def _is_general_knowledge_query(self, query: str) -> bool:
        query = query.lower()
        return any(kw in query for kw in self.general_knowledge_keywords)

    def _get_wikipedia_answer(self, query: str) -> str:
        if query in self.cache:
            return self.cache[query]
        
        try:
            result = wikipedia.summary(query, sentences=self.max_summary_length)
            self.cache[query] = result
            return result
        except wikipedia.DisambiguationError as e:
            raise
        except wikipedia.PageError:
            return self._answer_with_qa(query)
    
    def _answer_with_qa(self, question: str, context: str = "") -> str:
        if not context:
            context = question
        
        result = self.qa_pipeline(question=question, context=context)
        if result['score'] > 0.3:
            return result['answer']
        return "I don't have enough information to answer that."

# Create instance
knowledge_engine = KnowledgeEngine()
