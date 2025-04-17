from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from torch.utils.data import Dataset
import torch
import json
from utils.data_loader import DataLoader
import os

class ChatDataset(Dataset):
    def __init__(self, tokenizer, data, max_length=128):
        self.tokenizer = tokenizer
        self.input_ids = []
        self.attn_masks = []
        
        for item in data:
            encodings = tokenizer(item['prompt'], item['response'], 
                                 truncation=True, max_length=max_length, 
                                 padding='max_length')
            self.input_ids.append(torch.tensor(encodings['input_ids']))
            self.attn_masks.append(torch.tensor(encodings['attention_mask']))
    
    def __len__(self):
        return len(self.input_ids)
    
    def __getitem__(self, idx):
        return {
            'input_ids': self.input_ids[idx],
            'attention_mask': self.attn_masks[idx],
            'labels': self.input_ids[idx]
        }

def prepare_training_data():
    data_loader = DataLoader()
    data_loader.load_all_data()
    
    training_data = []
    
    # Convert all data to prompt-response pairs
    for category, items in data_loader.loaded_data.items():
        for item in items:
            if isinstance(item, dict):
                prompt = item.get('question', item.get('prompt', ''))
                response = item.get('answer', item.get('response', ''))
            else:
                prompt = f"Tell me about {category} {item[:20]}..."
                response = str(item)
            
            if prompt and response:
                training_data.append({'prompt': prompt, 'response': response})
    
    return training_data

def train_model():
    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    
    # Prepare data
    train_data = prepare_training_data()
    train_dataset = ChatDataset(tokenizer, train_data)
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=4,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=100,
        save_total_limit=2
    )
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )
    
    # Train
    trainer.train()
    
    # Save model
    model.save_pretrained('./saved_model')
    tokenizer.save_pretrained('./saved_model')

if __name__ == '__main__':
    train_model()