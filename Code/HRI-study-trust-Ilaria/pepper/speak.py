"""
This script connects to Pepper's Text-to-Speech (TTS) system and sends a text string to be spoken by Pepper.
Arguments:
- The script expects a single argument: the text to be spoken by Pepper.    
- If no argument is provided, it will print an error message and exit.
- The script uses the ALProxy class from the naoqi module to connect to Pepper's TTS system.
- The TTS proxy is initialized with the IP address and port of Pepper's TTS system. 
"""

import sys
from naoqi import ALProxy

def main(robot_ip):
    """Main function to run the script."""
    """ This function connects to Pepper's TTS and sends the text received as an argument. """
    if len(sys.argv) < 2:
        print("No input text received.")
        sys.exit(1)

    text = sys.argv[1]
    print("Received text: {}".format(text))  # Debugging line
    
    try:
        # Connect to Pepper's TTS (Text-to-Speech) proxy
        tts = ALProxy("ALTextToSpeech", robot_ip, 9559)
        tts.say(text)  # Pepper speaks the text
        print("Pepper is speaking.")  # Debugging line
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    robot_ip = "192.168.0.108" # Replace with your Pepper's IP address
    main(robot_ip)
