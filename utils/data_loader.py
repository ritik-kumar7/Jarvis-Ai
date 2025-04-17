import json
import os
import random

class DataLoader:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.loaded_data = {}
        
    def load_all_data(self):
        """Load all data from subdirectories"""
        for root, dirs, files in os.walk(self.data_dir):
            for file in files:
                if file.endswith('.json') or file.endswith('.jsonl'):
                    self._load_json_data(root, file)
                elif file.endswith('.txt') or file.endswith('.tsv'):
                    self._load_text_data(root, file)
    
    def _load_json_data(self, root, file):
        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f) if file.endswith('.json') else [json.loads(line) for line in f]
        
        category = os.path.basename(root)
        if category not in self.loaded_data:
            self.loaded_data[category] = []
        self.loaded_data[category].extend(data)
    
    def _load_text_data(self, root, file):
        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().splitlines()
        
        category = os.path.basename(root)
        if category not in self.loaded_data:
            self.loaded_data[category] = []
        self.loaded_data[category].extend(content)
    
    def get_random_response(self, category):
        """Get random response from a category"""
        if category in self.loaded_data and self.loaded_data[category]:
            return random.choice(self.loaded_data[category])
        return None