from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the tokenizer and model
model_name = "/Users/jaxsonpaige/.llama/checkpoints/Meta-Llama3.1-8B"  # or the Hugging Face model name if available
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Move the model to the GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Define input text for generation
input_text = "Once upon a time"

# Tokenize input text
inputs = tokenizer(input_text, return_tensors="pt").to(device)

# Generate text
output = model.generate(**inputs, max_length=50)

# Decode and print generated text
print(tokenizer.decode(output[0], skip_special_tokens=True))
