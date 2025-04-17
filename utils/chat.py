# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from .data_loader import DataLoader
# import re
# import math
# from .math_utils import MathSolver

# nltk.download('punkt')
# nltk.download('stopwords')

# class ChatSystem:
#     def __init__(self):
#         self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
#         self.data_loader = DataLoader()
#         self.data_loader.load_all_data()
#         self.stop_words = set(stopwords.words('english'))
#         self.context = {}
#         self.math_solver = MathSolver()
# class Jarvis:
#     def __init__(self):
#         self.math_solver = MathSolver()
        
#     def respond(self, query):
#         # Math detection
#         math_keywords = [
#             'calculate', 'solve', 'what is',
#             '+', '-', '*', '/', 'x', '^',
#             'derivative', 'integrate', '='
#         ]
        
#         if any(kw in query.lower() for kw in math_keywords):
#             return self.math_solver.solve_expression(query)
        
        

# class ChatSystem:
#     def __init__(self):
#         self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
#         self.data_loader = DataLoader()
#         self.data_loader.load_all_data()
#         self.stop_words = set(stopwords.words('english'))
#         self.context = {}
    
#     def preprocess_text(self, text):
#         text = text.lower()
#         text = re.sub(r'[^\w\s]', '', text)
#         tokens = word_tokenize(text)
#         tokens = [word for word in tokens if word not in self.stop_words]
#         return ' '.join(tokens)
    
#     def find_best_match(self, query, category):
#         query_embedding = self.model.encode([self.preprocess_text(query)])
        
#         if category not in self.data_loader.loaded_data:
#             return None
            
#         category_data = self.data_loader.loaded_data[category]
#         embeddings = self.model.encode([self.preprocess_text(str(item)) for item in category_data])
        
#         similarities = cosine_similarity(query_embedding, embeddings)
#         best_match_idx = np.argmax(similarities)
        
#         if similarities[0][best_match_idx] > 0.6:  # Threshold
#             return category_data[best_match_idx]
#         return None
    
#     def handle_math_queries(self, query):
#         try:
#             # Simple calculations
#             if 'calculate' in query or 'what is' in query:
#                 expr = re.findall(r'(\d+\s*[\+\-\*\/]\s*\d+)', query)
#                 if expr:
#                     result = eval(expr[0])
#                     return f"The result is: {result}"
            
#             # Algebra equations
#             if 'solve for x' in query:
#                 equation = query.split('solve for x in')[-1].strip()
#                 # Simple linear equation solver
#                 if '+' in equation:
#                     parts = equation.split('+')
#                     a = int(parts[0].split('x')[0]) if parts[0].split('x')[0] else 1
#                     b = int(parts[1])
#                     return f"Solution: x = {-b/a}"
#                 # Add more equation types here
                
#         except Exception as e:
#             return None
    
#     def respond(self, user_id, query):
#         # Check for math queries first
#         math_response = self.handle_math_queries(query)
#         if math_response:
#             return math_response
        
#         # Check different categories
#         categories = ['jokes', 'math', 'multipurpose', 'study_data', 'code_help']
#         for category in categories:
#             response = self.find_best_match(query, category)
#             if response:
#                 return response
        
#         # Default response if nothing matches
#         return "I'm still learning. Can you rephrase your question or ask something else?"


# utils/chat.py

from main import Jarvis

# Create one global Jarvis instance (backend)
jarvis_instance = Jarvis()

def get_jarvis_response(prompt: str) -> str:
    try:
        return jarvis_instance.respond(prompt)
    except Exception as e:
        return f"Error: {str(e)}"
