# -*- coding: utf-8 -*-

"""
This is a Flask web application that simulates an investment game.
The app allows users to invest money and receive returns based on a normal distribution.    

Author: Dharunkumar Senthilkumar    
Date: 2023-10-03
"""

from flask import Flask, render_template, request, jsonify
import subprocess
import csv
import os
from flask_cors import CORS
import gpt.gpt_interface as gpt
import threading
import utils.utils_func as utils
import time

# Initialize global variables
# These variables are used to store the state of the application and the user's data.
# They are initialized to default values and will be updated as the user interacts with the app.
bank = 10
person_id = 0
round_num = 0
investment = 0
returned = 0
classification = "Trustful" # Default classification is "Trustful"
money = 0 # Default money is 0

# chatgpt powered or not?
# This variable indicates whether the app is powered by GPT or not. It can be used to control the behavior of the app based on the GPT integration.
gpt_powered = "yes"  # Default is "not", indicating the app is not powered by GPT initially.

# Prompts 
system_prompt = f"""You're Pepper, a friendly humanoid robot created by SoftBank Robotics, here to chat, have fun, and run an engaging Investment Game experiment with humans.

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
    Assistant: I am {gpt_powered} powered by Gemini! I use a special version of Gemini to understand and respond to you. It’s like having a super brain!

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
    
    User: When will the experiment end?
    Assistant: It usually takes around 30 minutes, but it can vary.

    User: Can I leave the game in between?
    Assistant: Sure! You can leave anytime but it is encouraged to play the whole game. You don't need to tell me if you want to leave, and you can inform the researchers later.
    """

prompts =  {
    "start": """You're a friendly assistant introducing users to the Investment Game. Keep it welcoming, simple, and fun. Never mention the number of rounds.

            User: What is this app?
            Assistant: This is the Investment Game! Make smart choices, earn returns, and have fun!

            User: Can I start now?
            Assistant: Absolutely! You're all set. Let’s see how well you play this game.

            User: Is it hard?
            Assistant: Not at all! Just invest each round and see what comes back to you. I'm here to guide you!

            User: How many rounds are there?
            Assistant: Oh, that’s a surprise! Just focus on each round and enjoy the game.

            User: How much money do I have in bank and how much do I have?
            Assistant: You have 10 coins to start with. Let’s see how you can grow that!
            """ ,
    "invest": """You're the assistant prompting the user to invest. Stay neutral and encouraging. Keep responses short and clear. You can use playful language, but avoid being too casual.
            
            User: What should I do?
            Assistant: You have 10 coins. How much would you like to invest?

            User: Should I invest all?
            Assistant: That’s your choice! Just type how much you want to invest.

            User: Is there a trick?
            Assistant: No tricks—just trust, invest, and let’s see what happens!

            User: Can I invest less than 10?
            Assistant: Of course! You can invest any amount from 0 to 10 coins. What’s your choice?

            User: Can I invest 0?
            Assistant: You can invest 0 coins, but remember, no investment means no returns. What do you want to do?

            User: What is the logic behind the investment?
            Assistant: The logic is simple: invest wisely, and you might get more back. It’s all about trust and strategy!

            """,
    "think": """You're the assistant thinking about how much to return to the user. Keep it playful and mysterious.

            User: What’s going on?
            Assistant: Just thinking... Should I be generous this time? 

            User: Are you deciding now?
            Assistant: Yep! Calculating what to return... patience! 

            User: Why does it take time?
            Assistant: Gotta make sure it’s fair (or fun). Hang tight!
            """,
    "result": f"""You’re announcing the results of the round. Be cheerful, concise, and supportive. 

                User: What did I get back?
                Assistant: You invested {investment} coins, and I returned {returned}. Nice move!

                User: Was it good?
                Assistant: That was a smart investment. Let’s keep going!

                User: Did I win?
                Assistant: There’s no winning yet—just playing smart every round!

                Suppose the user lost money in this round.
                User: I lost money!
                Assistant: It happens! Every round is a new chance. Let’s see what you do next!

                Suppose the user won money in this round.
                User: I made money!
                Assistant: Awesome! You made {returned - investment} coins this round. Keep it up!

                User: How many rounds are left?
                Assistant: Oh, that’s a surprise! Just focus on each round and enjoy the game.

                User: What is the total amount in the bank?
                Assistant: The bank has {bank} coins now. Let’s see how you can grow that!
                """,

    "final": f"""You're wrapping up the game. Be warm, final, and positive. Don’t mention total rounds.

            User: Is it over?
            Assistant: Yep! That’s the end of the game. Great playing with you! You made some interesting choices. You can leave the game now.

            User: How did I do overall?
            Assistant: You made some bold moves! You made {bank} coins which is a great achievement. Hope you enjoyed the experience.

            User: Can I play again?
            Assistant: Unfortunately, this was a one-time game. But you played really well!
            """
}

conversation_history = [system_prompt] # This variable stores the conversation history with the GPT model. It is used to maintain context in the conversation.

current_prompt = prompts["start"]  # Default prompt to start the game

# Ensure the 'data' folder exists
os.makedirs("data", exist_ok=True)
log_file_path = "data/conversation.txt"

# Always ensure system prompt is in the log if not already
if not os.path.exists(log_file_path) or os.stat(log_file_path).st_size == 0:
    with open(log_file_path, "w", encoding="utf-8") as f:
        f.write(f"'role': 'system', 'content': {system_prompt}\n\n")

# Global variables for threading and stopping
current_thread = None
stop_event = None

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# CSV file path
# This file is used to store the results of the investment rounds. Each row in the CSV file corresponds to a round of investment and contains the relevant data.
CSV_FILE = "data/results.csv"    

# Create CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Person ID", "Round", "Investment", "Returned", "Classification", 'Person Money', 'Bank Money', 'GPT Powered'])

# Thread function to run Pepper script
def run_pepper_in_thread(command):
    """Runs the Pepper script in a background thread"""
    def _run():
        subprocess.run([
            r"S:\JOB\Amaneus\pepperchat\python.exe",
            r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py",
            command
        ])
    
    thread = threading.Thread(target=_run)
    thread.start()  # Runs in parallel
    # No need to join() - let it run independently

def start_new_thread(state_name, prompt):
    global current_thread, stop_event

    # Stop previous thread if running
    if stop_event is not None:
        stop_event.set()

    if current_thread is not None:
        current_thread.join()

    stop_event = threading.Event()
    current_thread = threading.Thread(
        target=gpt_communication,
        args=(state_name, prompt, stop_event),
        daemon=True
    )
    current_thread.start()


def gpt_communication(state_name, prompt, stop_event):
    """
    A continuous, always-listening loop:
        1) Speak the initial stage prompt once.
        2) Loop:
            • If no speech for 10 seconds → re-spark.
            • If user speaks:
                - If intent is "stop" → exit.
                - Else → respond.
        3) Exit only if stop_event is set or user says "stop".
    """

    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered, conversation_history

    max_retries = 2
    retry_count = 0
    conversation = conversation_history + [f"'role': 'system', 'content': {prompt}"] + ["Be engaging and don't repeat the sentences from the conversation before. Be short and concise. "]

    print(f"[{state_name.upper()}] Saying initial prompt.")
    gpt_response = gpt.generate_response(conversation, '.')
    conversation.append(f"'role': 'assistant', 'content': {gpt_response}'")

    # Speak initial prompt
    # Extract the last content from the GPT response
    extract_prompt = [f"""You will be given a text block containing nested role-content pairs like this:

                            Example input 1:
                            'role': 'assistant', 'content': Hello! How can I help you today?

                            Output 1:
                            Hello! How can I help you today?

                            Example input 2:
                            'role': 'assistant', 'content': 'role': 'assistant', 'content': I love talking to humans, sharing fun facts, and guiding you through the Investment Game. But really, I just want to be a good buddy during our time together!

                            Output 2:
                            I love talking to humans, sharing fun facts, and guiding you through the Investment Game. But really, I just want to be a good buddy during our time together!

                            Now, extract and clean the last assistant content from the following input text and output only that cleaned content without any extra quotes or metadata:

                            Input:
                            {gpt_response}

                            Output:"""]

    final_content = gpt.generate_response(extract_prompt, ".")
    if final_content:
        gpt.send_to_pepper(final_content)
        time.sleep(max(len(final_content) / 15, 2))
    else:
        print("No content found after initial prompt.")

    # Begin always-listening loop
    while not stop_event.is_set():
        user = gpt.get_user_message()  # Listen for 10 seconds max

        if user:
            # Reset retries
            retry_count = 0

            # Check if intent is to stop
            intent_prompt = (
                f"You are an intent classifier. The user said: '{user}'. "
                f"Does the user want to STOP the conversation? Reply only 'yes' or 'no' in lower case."
            )
            stop_intent = gpt.generate_response([intent_prompt], ".")
            if "yes" in stop_intent.lower():
                gpt.send_to_pepper("Okay, I'll stop for now. Talk to you later.")
                print(f"[{state_name.upper()}] Conversation ended by user.")
                break

            # Append user message and generate response
            conversation.append(f"'role': 'user', 'content': {user}")
            gpt_response = gpt.generate_response(conversation, '.')
            conversation.append(f"'role': 'assistant', 'content': {gpt_response}'")

            # Extract the last content from the GPT response
            extract_prompt = [f"""You will be given a text block containing nested role-content pairs like this:

                            Example input 1:
                            'role': 'assistant', 'content': Hello! How can I help you today?

                            Output 1:
                            Hello! How can I help you today?

                            Example input 2:
                            'role': 'assistant', 'content': 'role': 'assistant', 'content': I love talking to humans, sharing fun facts, and guiding you through the Investment Game. But really, I just want to be a good buddy during our time together!

                            Output 2:
                            I love talking to humans, sharing fun facts, and guiding you through the Investment Game. But really, I just want to be a good buddy during our time together!

                            Now, extract and clean the last assistant content from the following input text and output only that cleaned content without any extra quotes or metadata:

                            Input:
                            {gpt_response}

                            Output:"""]

            final_content = gpt.generate_response(extract_prompt, ".")
            if final_content:
                gpt.send_to_pepper(final_content)
                time.sleep(max(len(final_content) / 15, 2))
            else:
                print("No content found.")

        else:
            # No user input after timeout
            if retry_count < max_retries:
                spark_prompt = [
                    f"""You are a helpful assistant currently in the '{state_name}' stage of a conversation. 
                    The current topic is: {prompt}.\n. The user hasn’t responded for a while. 
                    Please generate a natural, engaging message to gently re-spark the conversation, as if continuing the discussion informally.
                    Ask a question or make a comment that relates to the current topic,
                    but keep it light and friendly. Avoid being too formal or robotic. Be concise and short. Don't repeat the sentences from the conversation before.
                    """
                ]
                spark_msg = gpt.generate_response(spark_prompt, ".")
                gpt.send_to_pepper(spark_msg)
                time.sleep(max(len(final_content) / 15, 2))
                retry_count += 1
            else:
                print(f"[{state_name.upper()}] No response after {max_retries + 1} retries. Exiting.")
                break

        # Log conversation after each turn
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(f"Round: {round_num}, Bank: {bank}, Person: {person_id}, "
                    f"Invested: {investment}, Returned: {returned}, "
                    f"Class: {classification}, Money Left: {money}, GPT: {gpt_powered}\n")
            for line in conversation:
                f.write(line + "\n")
            f.write("\n")

        # Update global conversation state
        conversation_history = conversation

    print(f"[{state_name.upper()}] Conversation loop exited.")

@app.route('/')
def index():    
    """ Main page of the app. """
    global gpt_powered, state_iterations, prompts
    
    subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"start"])
    
    if gpt_powered == "yes":
        current_prompt = prompts["start"]
        start_new_thread("index", current_prompt)

    return render_template('index.html')

@app.route('/invest_page')
def invest_page():
    """ Investment page of the app. """
    global gpt_powered, state_iterations, prompts
    
    if gpt_powered == "yes":
        current_prompt = prompts["invest"] 
        start_new_thread("invest", current_prompt)
    
    return render_template('invest_page.html')

@app.route('/thinking_page')
def thinking_page():
    """ Thinking page of the app. """
    global gpt_powered, state_iterations, prompts

    #subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"think"])
    #run_pepper_in_thread("think")

    if gpt_powered == "yes":
        current_prompt = prompts["think"] 
        start_new_thread("think", current_prompt)

    return render_template('thinking_page.html')

@app.route('/results_page')
def results_page():
    global classification, bank, investment, returned, round_num, gpt_powered, prompts

    status = "w" if classification == "Trustful" else "l"
    #subprocess.run([
     #       r"S:\JOB\Amaneus\pepperchat\python.exe",
      #      r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py",
       #     f"r{status}"
        #])
    run_pepper_in_thread(f"r{status}")

    if gpt_powered == "yes":
        current_prompt = prompts["result"]
        start_new_thread("result", current_prompt)

    return render_template(
        'results_page.html',
        round_num=round_num,
        investment=investment,
        returned=returned,
        bank=bank
    )

@app.route('/completion_page')
def completion_page():
    """ Completion page of the app. """
    global bank, gpt_powered, state_iterations, round_num, prompts

    #subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"final"])
    run_pepper_in_thread("final")
    if gpt_powered == "yes":
        current_prompt = prompts["final"] 
        start_new_thread("complete", current_prompt)
    
    bank = 10
    return render_template('completion_page.html', final_bank=bank, final_round=round_num)

@app.route('/invest', methods=['POST'])
def invest():
    """ Endpoint to handle investment data. """
    """ This endpoint receives investment data from the client, simulates a return amount, and saves the data to a CSV file. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400

    person_id = int(data.get('person_id'))
    round_num = int(data.get('round'))
    investment = int(data.get('investment'))

    if None in (person_id, round_num, investment):
        return jsonify({"error": "Missing required fields"}), 400

    # Simulate a return amount
    returned = utils.normal_random(investment)
    classification = "Trustful" if returned >= investment else "Untrustful"

    # Calculate new balances
    money = 10
    bank += (money + returned - investment)

    # Save to CSV
    with open(CSV_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            person_id, round_num, investment, 
            returned, classification, money, bank, gpt_powered
        ])

    return jsonify({
        "person_id": person_id,
        "round": round_num,
        "investment": investment,
        "returned": returned,
        "classification": classification,
        "money": money,
        "bank": bank
    })


if __name__ == '__main__':
    """ Main function to run the Flask app. """
    """ This function initializes the Flask app and the GPT communication thread. """

    # Start the Flask app
    # The app will run on all available IP addresses on port 5000. The debug mode is enabled for development purposes. In production, it should be disabled.
    # The app will be accessible at http://localhost:5000 and http://<your-ip>:5000

    app.run(host='0.0.0.0', port=5000, debug=True)