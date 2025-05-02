import time
from naoqi import ALProxy


class InvestmentGameReactions:
    def __init__(self, robot_ip, port=9559):
        # Initialize proxies for Pepper's modules
        self.robot_ip = robot_ip
        self.port = port
        self.tts = ALProxy("ALTextToSpeech", robot_ip, port)
        self.motion = ALProxy("ALMotion", robot_ip, port)
    
    # Start of the Game
    def start_game_reaction(self):
        print("Starting game...")
        self.tts.say("Welcome to the investment game!")
        self.motion.setStiffnesses("Head", 1.0)
        self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [0.0, -0.3], 0.2)
        time.sleep(1)
        self.motion.angleInterpolationWithSpeed(["HeadPitch"], [0.0], 0.2)

    # Invest Reaction
    def invest_reaction(self, trustful=True):
        print "Player is making an investment..."

        if trustful:
            self.tts.say("Great investment! You're on the right track!")
            
            # Raise both arms in a confident gesture
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                        "HeadYaw", "HeadPitch"]
            angles = [1.2, -0.2, 1.5, 0.8,
                    1.2, 0.2, -1.5, -0.8,
                    0.0, -0.1]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

        else:
            self.tts.say("Are you sure about that decision? Let's see how it goes.")

            # Open arms slightly with a tilted head (uncertainty gesture)
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                        "HeadYaw", "HeadPitch"]
            angles = [1.5, 0.4, 1.0, -0.3,
                    1.5, -0.4, -1.0, 0.3,
                    0.3, 0.2]
            speed = 0.4
            self.motion.angleInterpolationWithSpeed(joint_names, angles, speed)

        time.sleep(1)

    # Thinking 
    def thinking_action(self):
        print("Pepper is thinking...")

        # Set head to a thoughtful tilt
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

        # Return to neutral
        self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [0.0, 0.0], 0.3)
        self.motion.angleInterpolationWithSpeed(joint_names, [1.5, 0.0, 1.5, 0.0, 0.0], 0.3)

        print("Thinking gesture complete.")

    # Return Reaction
    def return_reaction(self, profit=0):
        print("Player received a return of %d" % profit)
        if profit > 0:
            self.tts.say("Great job! You made a profit of $%d!" % profit)
            self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RElbowRoll"], [1.0, 0.5], 0.4)
            self.motion.angleInterpolationWithSpeed(["LShoulderPitch", "LElbowRoll"], [1.0, -0.5], 0.4)
        else:
            self.tts.say("It looks like you lost a bit. Don't worry, try again!")
            self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RElbowRoll"], [0.4, -0.2], 0.4)
        time.sleep(1)

    # Trust or Untrust Reaction
    def trust_or_untrust_reaction(self, trustful=True):
        print("Player is deciding whether to trust...")
        if trustful:
            self.tts.say("I'm glad you trust the game!")
            self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RElbowRoll"], [0.8, 1.0], 0.5)
        else:
            self.tts.say("Are you sure about that decision?")
            self.motion.angleInterpolationWithSpeed(["HeadYaw", "HeadPitch"], [-0.3, 0.2], 0.3)
        time.sleep(1)

    # Next Round Reaction
    def next_round_reaction(self):
        print("Transitioning to the next round...")
        self.tts.say("Let's get ready for the next round!")
        time.sleep(1)


    # Final Completion Reaction
    def final_completion_reaction(self, final_balance=0):
        print("Game completed. Final balance: $%d" % final_balance)

        if final_balance > 1000:
            self.tts.say("Congratulations, you did an amazing job! Let's shake hands!")

            # Extend right arm for handshake
            self.motion.angleInterpolationWithSpeed([
                "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw2"
            ], [0.6, -0.2, 1.2, 0.5, 0.0], 0.3)

            time.sleep(1)

            # Simulate handshake motion (2 quick up-down movements)
            for _ in range(2):
                self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.3, 0.3)
                self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.5, 0.3)

            # Return to neutral
            self.motion.angleInterpolationWithSpeed([
                "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw2"
            ], [1.5, 0.0, 1.5, 0.0, 0.0], 0.3)

        else:
            self.tts.say("Better luck next time, you will do great!")
            self.motion.angleInterpolationWithSpeed(["HeadPitch"], [0.3], 0.4)

        time.sleep(1)


if __name__ == "__main__":
    robot_ip = "192.168.0.108"  # Replace with your Pepper's IP address
    game = InvestmentGameReactions(robot_ip)
    
    # Test the reactions step-by-step
    
    #game.start_game_reaction()
    #game.invest_reaction(trustful=False)
    #game.thinking_action()
    #game.return_reaction(profit=200)  # Test with profit
    #game.trust_or_untrust_reaction(trustful=False)
    game.next_round_reaction()
    #game.final_completion_reaction(final_balance=1500)  # Test with profit in final balance
