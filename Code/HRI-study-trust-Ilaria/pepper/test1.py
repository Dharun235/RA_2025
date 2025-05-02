import time
from naoqi import ALProxy


class InvestmentGameReactions:
    def __init__(self, robot_ip, port=9559):
        # Initialize proxies for Pepper's modules
        self.robot_ip = robot_ip
        self.port = port
        self.tts = ALProxy("ALTextToSpeech", robot_ip, port)
        self.motion = ALProxy("ALMotion", robot_ip, port)
        self.leds = ALProxy("ALLeds", robot_ip, port) 

    # Start Game Reaction
    def start_game_reaction(self):
        print("Starting game...")
        self.tts.say("Welcome to the investment game!")
        self.motion.setStiffnesses("Head", 1.0)
        
        # Head movement: initial look forward then slight nod to signify readiness
        self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [0.0, -0.3], 0.2)
        time.sleep(1)
        self.motion.angleInterpolationWithSpeed(["HeadPitch"], [0.0], 0.2)

        # Slight body tilt for engaging reaction
        self.motion.angleInterpolationWithSpeed("BodyPitch", 0.1, 0.3)
        self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)
        
        # LED color change: Green for start, signaling a positive, confident start
        self.leds.fadeRGB("FaceLeds", 0.0, 1.0, 0.0, 0.5)  # Green
        time.sleep(1)
        self.leds.fadeRGB("FaceLeds", 0.0, 0.0, 0.0, 0.5)  # Turn off Face LEDs

    # Invest Reaction
    def invest_reaction(self, trustful=True):
        print("Player is making an investment...")
        
        if trustful:
            self.tts.say("Great investment! You're on the right track!")
            
            # Raise both arms in a confident gesture (celebration)
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                            "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                            "HeadYaw", "HeadPitch"]
            angles = [1.2, -0.2, 1.5, 0.8, 1.2, 0.2, -1.5, -0.8, 0.0, -0.1]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

            # Head nod and subtle body sway for positive engagement
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.2, 0.2)
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.2)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.05, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Green to signal success and confidence
            self.leds.fadeRGB("FaceLeds", 0.0, 1.0, 0.0, 0.5)  # Green
        else:
            self.tts.say("Are you sure about that decision? Let's see how it goes.")
            
            # Open arms slightly with a tilted head (uncertainty gesture)
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                            "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                            "HeadYaw", "HeadPitch"]
            angles = [1.5, 0.4, 1.0, -0.3, 1.5, -0.4, -1.0, 0.3, 0.3, 0.2]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

            # Head tilt and questioning body gesture for doubt
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.3, 0.2)
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.3, 0.2)
            self.motion.angleInterpolationWithSpeed("BodyPitch", -0.05, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Yellow to signal caution or uncertainty
            self.leds.fadeRGB("FaceLeds", 1.0, 1.0, 0.0, 0.5)  # Yellow
        time.sleep(1)
        self.leds.fadeRGB("FaceLeds", 0.0, 0.0, 0.0, 0.5)  # Turn off LEDs

    # Thinking Action
    def thinking_action(self):
        print("Pepper is thinking...")
        
        # Set head to thoughtful tilt
        self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [0.2, 0.3], 0.3)
        
        # Bring right hand near the face (as if thinking)
        joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw2"]
        angles = [1.3, -0.2, 1.0, 1.2, 0.5]  # Adjust angles as needed to look natural
        self.motion.angleInterpolationWithSpeed(joint_names, angles, 0.3)

        time.sleep(1.5)

        # Slight head side tilt for emphasis
        self.motion.angleInterpolationWithSpeed("HeadYaw", -0.3, 0.2)
        time.sleep(1)
        self.motion.angleInterpolationWithSpeed("HeadYaw", 0.2, 0.2)

        # Return to neutral position
        self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [0.0, 0.0], 0.3)
        self.motion.angleInterpolationWithSpeed(joint_names, [1.5, 0.0, 1.5, 0.0, 0.0], 0.3)

        print("Thinking gesture complete.")

        # LED color change: Blue for thoughtfulness or contemplation
        self.leds.fadeRGB("FaceLeds", 0x0000FF)  # Blue
        time.sleep(1)
        self.leds.fadeRGB("FaceLeds", 0x000000)  # Turn off LEDs after reaction

    # Return Reaction
    def return_reaction(self, profit=0):
        print("Player received a return of %d" % profit)
        
        if profit > 0:
            self.tts.say("Great job! You made a profit of $%d!" % profit)
            self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RElbowRoll"], [1.0, 0.5], 0.4)
            self.motion.angleInterpolationWithSpeed(["LShoulderPitch", "LElbowRoll"], [1.0, -0.5], 0.4)

            # Confident body tilt and head nod to signal success
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.2, 0.2)
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.2)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.1, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Green to signify success
            self.leds.fadeRGB("FaceLeds", 0x00FF00)  # Green
        else:
            self.tts.say("It looks like you lost a bit. Don't worry, try again!")
            self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RElbowRoll"], [0.4, -0.2], 0.4)

            # Show empathy through concerned head tilt and body posture
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", -0.05, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Red for loss or disappointment
            self.leds.fadeRGB("FaceLeds", 0xFF0000)  # Red
        time.sleep(1)
        self.leds.fadeRGB("FaceLeds", 0x000000)  # Turn off LEDs after reaction

    # Trust or Untrust Reaction
    def trust_or_untrust_reaction(self, trustful=True):
        print("Player is deciding whether to trust...")
        
        if trustful:
            self.tts.say("I'm glad you trust the game!")
            
            # Thumbs-up gesture with both hands
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                            "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                            "HeadYaw", "HeadPitch"]
            angles = [1.2, -0.2, 1.5, 0.8, 1.2, 0.2, -1.5, -0.8, 0.0, -0.1]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

            # Head nod in affirmation
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.2, 0.2)
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.2)

            # LED color change: Green to signify trust
            self.leds.fadeRGB("FaceLeds", 0x00FF00)  # Green
        else:
            self.tts.say("Are you sure about that decision?")
            
            # Questioning gesture (arms bent)
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                            "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                            "HeadYaw", "HeadPitch"]
            angles = [1.5, 0.4, 1.0, -0.3, 1.5, -0.4, -1.0, 0.3, 0.3, 0.2]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

            # Head tilt and slight body sway for doubt
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.3, 0.2)
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.3, 0.2)
            self.motion.angleInterpolationWithSpeed("BodyPitch", -0.05, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Yellow to signal uncertainty
            self.leds.fadeRGB("FaceLeds", 0xFFFF00)  # Yellow

        time.sleep(1)
        self.leds.fadeRGB("FaceLeds", 0x000000)  # Turn off LEDs after reaction

    # Next Round Reaction
    def next_round_reaction(self):
        print("Transitioning to the next round...")
        self.tts.say("Let's get ready for the next round!")
        
        # Slight head movement to signify readiness and anticipation
        self.motion.angleInterpolationWithSpeed("HeadYaw", -0.2, 0.3)
        self.motion.angleInterpolationWithSpeed("HeadYaw", 0.2, 0.3)
        
        # Arms raised in an excited stance, preparing for next challenge
        joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                        "HeadYaw", "HeadPitch"]
        angles = [1.2, -0.2, 1.5, 0.8, 1.2, 0.2, -1.5, -0.8, 0.0, -0.1]
        speed = 0.4
        self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

        # LED color change: Blue to signal transition or excitement
        self.leds.fadeRGB("FaceLeds", 0x0000FF)  # Blue
        time.sleep(1)
        self.leds.fadeRGB("FaceLeds", 0x000000)  # Turn off LEDs after reaction

    # Final Completion Function
    def final_completion_reaction(self, result):
        if result == "win":
            print("Congratulations, you won the game!")
            self.tts.say("Congratulations! You've won the game!")
            
            # Celebrate with arms raised and a confident head nod
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                            "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                            "HeadYaw", "HeadPitch"]
            angles = [1.5, -0.2, 1.5, 0.8, 1.5, 0.2, -1.5, -0.8, 0.0, -0.1]
            speed = 0.5
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)
            
            # Confident head nods and body posture to show victory
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.2, 0.3)
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.1, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Green to signify victory
            self.leds.fadeRGB("FaceLeds", 0x00FF00)  # Green for success
        elif result == "lose":
            print("Sorry, you lost the game!")
            self.tts.say("Unfortunately, you lost the game. Better luck next time.")
            
            # Show empathy with a tilted head and arms lowered
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                            "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                            "HeadYaw", "HeadPitch"]
            angles = [1.0, 0.4, 1.0, -0.3, 1.0, -0.4, -1.0, 0.3, 0.3, 0.2]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

            # Tilt head slightly down for disappointment
            self.motion.angleInterpolationWithSpeed("HeadPitch", 0.3, 0.3)
            self.motion.angleInterpolationWithSpeed("HeadPitch", -0.3, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", -0.1, 0.3)
            self.motion.angleInterpolationWithSpeed("BodyPitch", 0.0, 0.3)

            # LED color change: Red to signify loss
            self.leds.fadeRGB("FaceLeds", 0xFF0000)  # Red for failure
        else:
            print("Game ended with no winner or loser.")
            self.tts.say("The game has ended.")
            
            # Return to neutral position
            self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [0.0, 0.0], 0.3)
            self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RElbowRoll"], [1.5, 0.0], 0.3)
            self.motion.angleInterpolationWithSpeed(["LShoulderPitch", "LElbowRoll"], [1.5, 0.0], 0.3)

            # LED color change: Blue to signify neutral state (game end)
            self.leds.fadeRGB("FaceLeds", 0x0000FF)  # Blue for neutrality
            time.sleep(1)
            self.leds.fadeRGB("FaceLeds", 0x000000)  # Turn off LEDs after reaction
    

if __name__ == "__main__":
    robot_ip = "192.168.0.108"  # Replace with your Pepper's IP address
    pepper_game = InvestmentGameReactions(robot_ip)
    
    # Test the reactions step-by-step
    #pepper_game.start_game_reaction()
    #pepper_game.invest_reaction(trustful=True)  # Or False based on your test case
    #pepper_game.thinking_action()
    #pepper_game.return_reaction(profit=200)  # Example profit value
    #pepper_game.trust_or_untrust_reaction(trustful=False)  # Or False
    #pepper_game.next_round_reaction()
    pepper_game.final_completion_reaction(result="win")  # Example balance    
