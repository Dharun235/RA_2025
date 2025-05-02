from google import genai
import speech_recognition as sr
import subprocess
import keyboard

client = genai.Client(api_key="AIzaSyC3NHq1XSTbgtEcxo4w4in-toMicl4asig")
myfile = client.files.upload(file="sample_recording.m4a")
prompt = "Respond in a polite way and also shorter in tamil language"

def get_user_message():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

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


response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[prompt, get_user_message()]
    )
print(response.text)
send_to_pepper(response.text) 
