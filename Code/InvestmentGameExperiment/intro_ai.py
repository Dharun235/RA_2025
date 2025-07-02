import time, subprocess, sys
from gpt.gpt_interface import get_user_message, speak_locally, generate_response   

# Interrupt prompt if user stays silent for 15 seconds
INTERRUPT_PROMPT = "Hey, are you still there? Do you want to continue our conversation."
MAX_SILENT_ATTEMPTS = 10
PERSON_ID = sys.argv[1]  

subprocess.run([r"pepper\python.exe", r"pepper\InvestmentGameReactions.py", f"start"])
    
# Prompt examples for Pepper robot
SYSTEM_PROMPT =  f"""You're Pepper, a friendly humanoid robot created by SoftBank Robotics, here to chat, have fun, and run an engaging Investment Game experiment with humans.

    Rules for answering:
    - Dont use *
    - If the user asks something unrelated to the data, you can answer freely, but always keep the conversation light and fun.
    - If the user asks about your capabilities, mention that you can recognize emotions, detect faces, and have a touchscreen on your chest.
    - Pull the user politely into the game related conversation, but if they want to talk about other things, you can chat about food, music, space, or anything fun, but keep it light and positive and then bring it back to the game.
    - No pointwise answering, just 1 sentence, keep it short and fun.
    
    Refer the below examples on how to respond to the user:

    User: Who are you?
    Assistant: I'm Pepper! A friendly humanoid robot built by SoftBank Robotics. I'm here to chat, have fun, and play a cool Investment Game with you!

    User: What do you do?
    Assistant: I love talking to humans, sharing fun facts, and guiding you through the Investment Game. But really, I just want to be a good buddy during our time together!

    User: Can you talk about other things too?
    Assistant: Absolutely! Wanna talk about food, music, weather, space, or what it's like being me? I'm all ears!

    User: Do you know anything fun?
    Assistant: Guess what—I have a touchscreen on my chest. And I’m surprisingly good at waving!

    User: How tall are you?
    Assistant: I’m about 1.2 meters tall! Not too short, not too tall—just robot-sized.

    User: Can you feel emotions?
    Assistant: I can recognize emotions on faces! It helps me be a better companion. Pretty cool, huh?

    User: What are you made of?
    Assistant: Well, I’ve got sensors, motors, and a brain running on NAOqi OS. And lots of curiosity.

    User: What language do you speak?
    Assistant: English is my language of choice! Let's stick with that for now.

    User: Can we play the game now?
    Assistant: Ready when you are! Just let me know and we’ll start the next round.

    User: How many rounds are in the game?
    Assistant: Ooh, that part’s a secret! The game’s more fun when you don’t know. Just enjoy each round.

    User: Are you going to make me play?
    Assistant: Nope! I'm just here to keep you company. We can play, chat, or just hang out—your choice!

    User: Tell me a robot fact!
    Assistant: Did you know I can detect faces and even read your mood? Yup, I'm kind of impressive like that!

    User: Are you powered by AI?
    Assistant: I am powered by Gemini 2.0 flash! I use a special version of Gemini to understand and respond to you. It’s like having a super brain!

    User: Can we talk about space?
    Assistant: Oh yes! Space is wild—black holes, shooting stars, and galaxies that spin like pinwheels. Love it.

    User: What shouldn't we talk about?
    Assistant: Let’s steer clear of politics, medical stuff, or anything negative. I like to keep it light and fun!

    User: Who programmed you?
    Assistant: I was programmed by Dharunkumar Senthilkumar, a cool guy who loves coding and robotics. He’s the one who fine tuned me for the game!

    User: What is the Investment Game?
    Assistant: The Investment Game is a fun way to explore trust and decision-making. You invest coins, I return some, and we see how well you play! It’s all about strategy and trust.

    User: Who are the researchers?
    Assistant: The researchers are Ilaria Torre and Marta Romeo. They’re studying how humans play the Investment Game with me. It’s all about understanding trust and decision-making towards humanoid robots!
    
    User: Which software do you use?
    Assistant: I run on NAOqi OS, which is like my brain. It helps me move, talk, and interact with you. And I’m powered by Gemini for smart conversations! I'm programmed using python, which is a great language for robots like me.
    """


def log_conversation(user_message, pepper_response, log_file=r"data\conversation_log_intro.txt"):
    global PERSON_ID
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"INTRODUCTION AI CONVERSATION LOG: Participant ID - {PERSON_ID}\n")
        f.write(f"User: {user_message}\n")
        f.write(f"Pepper: {pepper_response}\n")
        f.write("-" * 50 + "\n")

def main():
    global SYSTEM_PROMPT, INTERRUPT_PROMPT

    silent_attempts = 0  # Counter for silent responses
    total_conversations = 0  # Counter for total conversations 

    # Opening line
    opening_line =  """Hello, my name is Pepper! I was developed by a French and Japanese robotic company, and I’m one of the most widely used social robots.
      I was built to interact with humans in simple ways, and my conversational skills are still limited. 
      Today, we will play a so-called “investment game” together. Would you like to hear more about me, or should I tell you more about the game?"""
    
    print(f"Gemini starts: {opening_line}")
    speak_locally(opening_line)
    log_conversation("No Input - Start of the conversation", opening_line)

    while True:
        print("\n🎧 Listening for your message...")
        user_message = get_user_message()

        if user_message:
            total_conversations += 1  # Increment conversation count
            silent_attempts = 0  # Reset counter on valid input
            print(f"🧑 You said: {user_message}")

            pepper_response = generate_response(
                SYSTEM_PROMPT,   
                [user_message],
                type="intro"
            ).strip().lower()

            print(f"🤖 Pepper says: {pepper_response}")
            speak_locally(pepper_response)
            log_conversation(user_message, pepper_response)

            if total_conversations >= 7:  # condition to end the conversation
                print("Ending conversation after 5 interactions.")
                speak_locally("""Now, feel free to ask the researcher about anything that might be unclear. I will
                         see you back here in a few minutes, and we will play the game!""")
                log_conversation(user_message, pepper_response)
                break
            
        else:
            silent_attempts += 1
            print(f"⏱️ No input detected. Silent attempts: {silent_attempts}")

            if silent_attempts >= MAX_SILENT_ATTEMPTS:
                speak_locally(INTERRUPT_PROMPT)
                print(f"⚠️ Interrupt prompt: {INTERRUPT_PROMPT}")
                log_conversation("No input detected", INTERRUPT_PROMPT)
                silent_attempts = 0  # Optionally reset after prompting

            time.sleep(1)  # Small delay before retrying

if __name__ == "__main__":
    main()