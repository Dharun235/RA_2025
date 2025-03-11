import sys
from naoqi import ALProxy

def main():
    if len(sys.argv) < 2:
        print("No input text received.")
        sys.exit(1)

    text = sys.argv[1]
    print("Received text: {}".format(text))  # Debugging line
    
    try:
        # Connect to Pepper's TTS (Text-to-Speech) proxy
        tts = ALProxy("ALTextToSpeech", "192.168.0.106", 9559)
        tts.say(text)  # Pepper speaks the text
        print("Pepper is speaking.")  # Debugging line
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
