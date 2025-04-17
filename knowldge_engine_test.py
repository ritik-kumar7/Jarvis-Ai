from utils.knowledge_engine import knowledge_engine  # Import the instance, not the class

def test_queries():
    test_cases = [
        # History & Famous People
        "Who was the first president of the United States?",
        "Tell me about the history of the Great Wall of China.",
        "What is the significance of the Battle of Waterloo?",
        
        # Geography
        "Where is Mount Everest located?",
        "What is the longest river in the world?",
        "Can you tell me the capital of France?",

        # Science
        "How does the human brain work?",
        "What is the theory of relativity?",
        "Explain how vaccines work.",

        # Technology
        "What is machine learning?",
        "Tell me about the development of the internet.",
        "How do smartphones work?",

        # Space & Astronomy
        "What is a black hole?",
        "Tell me about the first moon landing.",
        "How do rockets work?",

        # Literature & Arts
        "Who wrote 'Romeo and Juliet'?",
        "What are the main themes in '1984' by George Orwell?",
        "Tell me about the Renaissance period in art.",

        # Health & Medicine
        "What causes the common cold?",
        "How does the human circulatory system function?",
        "Tell me about the discovery of penicillin."
    ]
    
    for i, query in enumerate(test_cases, 1):
        print(f"\nTest {i}: {query}")
        answer = knowledge_engine.handle(query)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    test_queries()
