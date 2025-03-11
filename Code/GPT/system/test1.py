import subprocess
import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

# Load DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone for recording
    with sr.Microphone() as source:
        print("Say something...")  # Prompt user to speak
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to audio

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def generate_gpt_response(text):
    # Encode the input text and generate a response from the model
    new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
    bot_input_ids = new_user_input_ids
    chat_history_ids = None

    # Generate response from DialoGPT
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id, 
                                      do_sample=True, top_k=50, top_p=0.95, temperature=0.7, 
                                      repetition_penalty=1.5, length_penalty=1.0)
    
    # Decode the generated response
    chat_history_ids = chat_history_ids[:, bot_input_ids.shape[-1]:]  # Get only the last response
    response = tokenizer.decode(chat_history_ids[0], skip_special_tokens=True)
    
    print(f"DialogGPT Response: {response}")
    return response

def send_to_pepper(text):
    if not text:
        print("No text to send to Pepper!")
        return

    # Debugging: print what is being sent to Pepper
    print(f"Sending to Pepper: {text}")

    try:
        # Use subprocess to run the Python 2 script with the text input
        result = subprocess.run([r"S:/JOB/Amaneus/pepperchat/python.exe", "test2.py", text], capture_output=True, text=True)
        print(f"Pepper's response: {result.stdout.strip()}")  # Debug line

        # Optionally print stderr if there is an error
        if result.stderr:
            print(f"Error: {result.stderr.strip()}")
    except Exception as e:
        print(f"Error sending text to Pepper: {e}")

def main():
    while True:
        text = recognize_speech()  # Record and convert speech to text
        if text:
            gpt_response = generate_gpt_response(text)  # Generate response from DialogGPT
            send_to_pepper(gpt_response)  # Send the generated response to Pepper for speech
        time.sleep(1)  # Small delay before the next loop iteration (can adjust the value)

if __name__ == "__main__":
    main()
