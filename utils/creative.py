from transformers import pipeline

from utils.brain import BaseSolver
from .base_solver import BaseSolver
class CreativeWriter(BaseSolver):
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2-medium")
    
    def handle(self, query: str, context: str = "") -> str:
        try:
            if 'poem' in query:
                return self._generate_poem(query)
            elif 'story' in query:
                return self._generate_story(query)
            return self._generic_generation(query)
        except Exception as e:
            return f"Creative error: {str(e)}"

    def handle(self, query: str, context: str = "") -> str:
        query = query.lower()
        
        if 'poem' in query:
            return self._generate_poem(query)
        elif 'story' in query:
            return self._generate_story(query)
        elif any(term in query for term in ['write', 'create', 'generate']):
            return self._generic_generation(query)
        else:
            return "I can write poems, stories, or other creative content."
    
    def _generate_poem(self, query: str) -> str:
        try:
            topic = query.replace('poem', '').replace('about', '').split('in')[0].strip()
            style = "modern" if "style" not in query else query.split('in')[-1].replace('style', '').strip()
            
            prompt = self.poem_prompt.format(topic=topic, style=style)
            poem = self.generator(prompt, max_length=150, do_sample=True)[0]['generated_text']
            return poem.split("\n")[-1]  # Return only the generated part
        except Exception as e:
            return f"Couldn't compose poem: {str(e)}"
    
    def _generate_story(self, query: str) -> str:
        try:
            prompt = f"Write a short story about {query.replace('story', '').replace('about', '').strip()}:\n"
            story = self.generator(prompt, max_length=300, do_sample=True)[0]['generated_text']
            return story.split("\n")[-1]
        except Exception as e:
            return f"Couldn't generate story: {str(e)}"
    
    def _generic_generation(self, query: str) -> str:
        try:
            result = self.generator(query, max_length=200, do_sample=True)[0]['generated_text']
            return result
        except Exception as e:
            return f"Couldn't generate content: {str(e)}"