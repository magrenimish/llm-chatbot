from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from dotenv import load_dotenv
load_dotenv()

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,      # use float32 on CPU
    device_map="auto"
)

def ask_llm(message: str) -> str:
    prompt = f"<|system|>\nYou are a helpful medical assistant.\n<|user|>\n{message}\n<|assistant|>"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.split("<|assistant|>")[-1].strip()
