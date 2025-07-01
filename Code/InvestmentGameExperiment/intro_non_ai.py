import time, subprocess
from gpt.gpt_interface import get_user_message, speak_locally, generate_response   

# Interrupt prompt if user stays silent for 15 seconds
INTERRUPT_PROMPT = "Hey, are you still there? Do you want to continue our conversation."
MAX_SILENT_ATTEMPTS = 10

subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"start"])
    
# Dialogues for Pepper robot
pepper_dialogues = {"Intro": """Hello, my name is Pepper! I was developed by a French and Japanese robotic
                        company, and I’m one of the most widely used social robots. I was built to interact
                        with humans in simple ways, and my conversational skills are still limited. Today, we
                        will play a so-called “investment game” together. Would you like to hear more about
                        me, or should I tell you more about the game?
                        Option 1: robot
                        Option 2: game """,
                    "robot": """Okay! I’m a social robot, made by a company called SoftBank Robotics. I can
                        move my arms, show expressions with my eyes, and talk using a speaker in my
                        chest. I don’t actually think though, I follow a script like a play. Would you like to know
                        how I was programmed, or should I tell you about the game now? 
                        Option 1: programme
                        Option 2: game""",
                    "programme": """I was programmed using a rule-based system. That means I respond
                        based on what people say, but only if they use specific words I recognize. So if you
                        say something I don’t expect, I might not reply properly. Sorry in advance! Are you
                        ready to hear about the game, or do you want to hear a cool fact about robots?
                        Option 1: cool fact
                        Option 2: game""",
                    "cool fact": """Ok, here it is. Currently, there is a robot, Sophia by Hanson Robotics, who
                        is an official citizen of Saudi Arabia. It was the first robot in history to receive legal
                        personhood, in 2017! Now, let’s talk about the game.""",
                    "game": """Great! In this game, we’ll play a game called “the investment game”. You’ll
                        start each round with 10 experimental dollars. You can give some, all, or none of
                        those dollars to me. If you give me any dollars, the amount you invest will be tripled.
                        I’ll then decide how many dollars to return to you. I can return none, some, or all. The
                        goal for both of us is to make as much money as possible.""",
                    "final": """Now, feel free to ask the researcher about anything that might be unclear. I will
                        see you back here in a few minutes, and we will play the game!"""}
def main():
    global pepper_dialogues, INTERRUPT_PROMPT

    silent_attempts = 0  # Counter for silent responses

    # Opening line
    opening_line = pepper_dialogues["Intro"]
    pepper_dialog_present = opening_line
    print(f"Gemini starts: {opening_line}")
    speak_locally(opening_line)

    while True:
        print("\n🎧 Listening for your message...")
        user_message = get_user_message()

        if user_message:
            silent_attempts = 0  # Reset counter on valid input
            print(f"🧑 You said: {user_message}")

            classifier = generate_response(
                """You are a classifier to output whether the user said as one of these as options and try to match one of these only and not any other very similar words, so only these - robot or game or final or cool fact or programme. If not, give the output as nothing."
                    You should only output the classifier as one of these options, and not any other similar words. You are provided with a message - {opening_line} to use to classify the user's input. You can also refer to the message if you dont understand the user's input.
                    For example,
                    1. if the user says "Tell me about the robots", you should output "robot" and not "robot"
                    2. if the user says "I want to know about the game", you should output "game" and not "gameplay."
                    3. if the user says "I want to know about the final", you should output "final" and not "finale"
                    4. if the user says "I want to know about the cool fact", you should output "cool fact" and not "cool facts"
                    5. if the user says "I want to know about the programme", you should output "programme" and not "programming"
                    6. if the user says "I want to know about the robot", you should output "robot" and not "robotics"
                    7. if the user says "I want to end the game", you should output "final" and not "end".
                    8. If the user says option, you should refer to the message and use that to classify into robot or game or final or cool fact or programme.
                """,
                [user_message],
                type="intro"
            ).strip().lower()

            print(f"🤖 Classifier says: {classifier}")

            if classifier == "nothing":
                print("❌ Classifier did not match any valid options.")
                speak_locally("Could you please repeat or choose one of the options I mentioned? Here are the options again: robot, game, final, cool fact, or programme.")
            else:
                response = pepper_dialogues[classifier]
                speak_locally(response)

                if classifier == "cool fact":
                    speak_locally(pepper_dialogues["game"])
                    speak_locally(pepper_dialogues["final"])
                    break

                if classifier == "game": 
                    speak_locally(pepper_dialogues["final"])
                    break

                if classifier == "final":
                    break
        else:
            silent_attempts += 1
            print(f"⏱️ No input detected. Silent attempts: {silent_attempts}")

            if silent_attempts >= MAX_SILENT_ATTEMPTS:
                speak_locally(INTERRUPT_PROMPT)
                print(f"⚠️ Interrupt prompt: {INTERRUPT_PROMPT}")
                silent_attempts = 0  # Optionally reset after prompting

            time.sleep(1)  # Small delay before retrying

if __name__ == "__main__":
    main()