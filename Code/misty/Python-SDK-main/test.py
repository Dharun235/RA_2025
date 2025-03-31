from mistyPy.Robot import Robot

# Initialize Misty Robot
misty = Robot("192.168.0.105")  # Replace with your Misty robot's IP address

# Function to handle speech capture and response
def capture_and_respond():
    # Speak a greeting
    misty.speak("Hello! Please say something.", 1, 1, "en-us")
    
    # Capture speech and respond with what was captured
    result = misty.speak_and_listen("Speak now...", 10000, False)
    
    # Parse the result (Access the response JSON)
    if result.status_code == 200:
        response_data = result.json()  # Get the response JSON data
        if 'message' in response_data and 'text' in response_data['message']:
            print(f"You said: {response_data['message']['text']}")
            misty.speak(f"You said: {response_data['message']['text']}", 1, 1, "en-us")
        else:
            print("No speech detected.")
    else:
        print("Error in capturing speech.")

# Call the function to capture and respond
capture_and_respond()
