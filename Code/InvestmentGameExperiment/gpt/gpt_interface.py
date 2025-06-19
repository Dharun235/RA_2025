"""
This script connects to Pepper's Text-to-Speech (TTS) system and sends a text string to be spoken by Pepper.
It is designed to be run from the command line with the text to be spoken as an argument.
It uses the ALProxy class from the naoqi module to connect to Pepper's TTS system.
It initializes the TTS proxy with the IP address and port of Pepper's TTS system. 
It includes methods for different game reactions, such as starting the game, investing, thinking, and showing results."""

from google import genai
import speech_recognition as sr
import subprocess

# Client initialization for Google GenAI
client = genai.Client(api_key="AIzaSyC3NHq1XSTbgtEcxo4w4in-toMicl4asig") # Replace with your actual API key

def get_user_message():
    """Capture audio from the microphone and return recognized text.
       If timeout is provided, it will wait at most that many seconds for speech.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now…")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            # No speech detected within the timeout
            print("❌ Timeout — no speech detected")
            return ""
    try:
        user_message = recognizer.recognize_google(audio)
        print("📝 You said:", user_message)
        return user_message
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")
        return ""

def send_to_pepper(text):
    """Function to send text to Pepper."""
    """ This function uses subprocess to run a Python 2 script that sends the text to the Pepper robot. """
    if not text:
        print("No text to send to Pepper!")
        return

    # Debugging: print what is being sent to Pepper
    print(f"Sending to Pepper: {text}")

    try:
        # Use subprocess to run the Python 2 script with the text input
        result = subprocess.run([r"S:/JOB/Amaneus/pepperchat/python.exe", "pepper/speak.py", text], capture_output=True, text=True)
        print(f"Pepper's response: {result.stdout.strip()}")  # Debug line

        # Optionally print stderr if there is an error
        if result.stderr:
            print(f"Error: {result.stderr.strip()}")
    except Exception as e:
        print(f"Error sending text to Pepper: {e}")

def generate_response(prompt, user_message):
    """Function to generate a response using Google GenAI."""
    """ This function uses the Google GenAI client to generate a response based on the prompt and user message. """
    # Use the Google GenAI client to generate a response
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[prompt, user_message]
    )
    return response.text

