from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load DialoGPT
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "No input received"})

    # Encode input
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Generate response
    response_ids = model.generate(input_ids, max_length=1000, do_sample=True, temperature=0.7)
    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Runs API locally
