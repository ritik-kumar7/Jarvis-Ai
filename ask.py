import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def debug_jarvis(prompt, model_path="./jarvis_models/code_help"):
    print(f"🔍 Loading tokenizer from: {model_path}")
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    category_prompt = f"[code_help] {prompt}"
    print(f"🧠 Full input prompt: {category_prompt}")
    
    inputs = tokenizer.encode(category_prompt, return_tensors="pt").to(device)
    print(f"🧪 Input tokens: {inputs}")

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=150,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.9,
            num_return_sequences=1
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"\n📦 Decoded Output:\n{decoded}")

    if category_prompt in decoded:
        completion = decoded.replace(category_prompt, "").strip()
    else:
        completion = decoded.strip()

    print("\n✅ Final Cleaned Completion:")
    print(completion if completion else "[EMPTY OUTPUT ❌]")

if __name__ == "__main__":
    prompt = input("🧠 Ask Jarvis (code_help): ")
    debug_jarvis(prompt)
