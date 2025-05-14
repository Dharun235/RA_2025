"""
This script connects to Pepper's Text-to-Speech (TTS) system and sends a text string to be spoken by Pepper.    
Arguments:
- The script expects a single argument: the text to be spoken by Pepper.
    - If no argument is provided, it will print an error message and exit.
    - The script uses the ALProxy class from the naoqi module to connect to Pepper's TTS system.
    - The TTS proxy is initialized with the IP address and port of Pepper's TTS system.
    
Additional functionality:
- The script includes methods for different game reactions, such as starting the game, investing, thinking, and showing results.
- Each method is designed to handle specific reactions and interactions with the user.

"""


from naoqi import ALProxy
import sys

class InvestmentGameReactions:
    def __init__(self, robot_ip, port=9559):
        # Initialize proxies for Pepper's modules
        self.robot_ip = robot_ip
        self.port = port
        self.tts = ALProxy("ALTextToSpeech", robot_ip, port)
        self.motion = ALProxy("ALMotion", robot_ip, port)
        self.leds = ALProxy("ALLeds", robot_ip, port) 

    # Start Game Reaction
    def start_game_reaction(self, text):
        pass

    # Invest Reaction
    def invest_reaction(self, text):
        pass

    # Thinking Action
    def thinking_action(self, text):
        pass

    # Result Reaction
    def result_reaction(self, text):
        pass

    # Final Completion Function
    def final_completion_reaction(self, text):
        pass
    

if __name__ == "__main__":
    robot_ip = "192.168.0.108"  # Replace with your Pepper's IP address
    pepper_game = InvestmentGameReactions(robot_ip)
    text_received = sys.argv[1]
    func_call, speak_text = text_received.split("//")

    # Call the appropriate function based on the received text
    # Test the reactions step-by-step
    if text_received == "start":
        pepper_game.start_game_reaction(speak_text)
    elif text_received == "invest":
        pepper_game.invest_reaction(speak_text)  
    elif text_received == "think":
        pepper_game.thinking_action(speak_text)
    elif text_received == "result":
        pepper_game.result_reaction(speak_text)
    elif text_received == "final":
        pepper_game.final_completion_reaction(speak_text)  
