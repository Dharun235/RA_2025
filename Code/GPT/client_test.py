import requests
import json
from naoqi import ALProxy

# Set the IP of your PC running DialoGPT
DIALOGPT_SERVER_IP = "192.168.0.101"  # Change this to your PC's IP
DIALOGPT_SERVER_PORT = 5000

# Connect to Pepper's text-to-speech module
PEPPER_IP = "127.0.0.1"  # Change this to Pepper's IP
PEPPER_PORT = 9559
tts = ALProxy("ALTextToSpeech", PEPPER_IP, PEPPER_PORT)

def chat_with_dialoGPT(user_message):
    try:
        url = "http://{}:{}/chat".format(DIALOGPT_SERVER_IP, DIALOGPT_SERVER_PORT)
        headers = {"Content-Type": "application/json"}
        data = json.dumps({"message": user_message})

        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        return response_data.get("response", "I didn't understand.")
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")  # Python 2
        if user_input.lower() == "exit":
            break
        
        response = chat_with_dialoGPT(user_input)
        print("AI: " + response)

        # Let Pepper speak the response
        tts.say(response)
