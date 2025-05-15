"""
This is a Flask web application that simulates an investment game.
The app allows users to invest money and receive returns based on a normal distribution.    

Author: Dharunkumar Senthilkumar    
Date: 2023-10-03
"""

from flask import Flask, render_template, request, jsonify
import subprocess
import random
import csv
import os
from flask_cors import CORS
import random
import numpy as np
import gpt.gpt_interface as gpt
import time
import threading

# Initialize global variables
# These variables are used to store the state of the application and the user's data.
# They are initialized to default values and will be updated as the user interacts with the app.
bank = 0
person_id = 0
round_num = 0
investment = 0
returned = 0
classification = "Trustful" # Default classification is "Trustful"
money = 0 # Default money is 0
conversation_history = [] # This variable stores the conversation history with the GPT model. It is used to maintain context in the conversation.


# chatgpt powered or not?
# This variable indicates whether the app is powered by GPT or not. It can be used to control the behavior of the app based on the GPT integration.
gpt_powered = "yes"
if gpt_powered == "yes":
    timer = random.randint(3, 6)
else:
    timer = random.randint(1, 3)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# CSV file path
# This file is used to store the results of the investment rounds. Each row in the CSV file corresponds to a round of investment and contains the relevant data.
CSV_FILE = "data/results.csv"    

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Create CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Person ID", "Round", "Investment", "Returned", "Trustful", 'Person Money', 'Bank Money', 'GPT Powered'])


# Function to generate a normal distribution of returns
def normal_random(investment):
    """ Function to generate a normal distribution of returns. 
    This function simulates a normal distribution of returns based on the investment amount."""
    # Define the range of possible return values
    max_return = 3 * (investment)
    min_return = 0
    
    # Define the midpoint of the range
    mid_point = (max_return) // 2
    
    # Set the standard deviation for the normal distribution - Standard deviation controls the spread. A smaller value gives a narrower peak, and a larger value gives a wider one.
    std_dev = max_return / 6  # This is a typical choice for normalization

    # Generate a random number from a normal distribution centered at mid_point
    value = np.random.normal(mid_point, std_dev)
    
    # Clip the value to ensure it's within the valid range [min_return, max_return]
    value = max(min_return, min(max_return, round(value)))
    
    return value


@app.route('/')
def index():    
    """ Main page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    prompt = ""
    question = ""
    gpt_response = gpt.generate_response(prompt,question)
    time.sleep(timer)
    subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"start//{gpt_response}"])
    return render_template('index.html')

@app.route('/invest_page')
def invest_page():
    """ Investment page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    prompt = ""
    question = ""
    gpt_response = gpt.generate_response(prompt,question)
    time.sleep(timer)
    subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"invest//{gpt_response}"])
    return render_template('invest_page.html')

@app.route('/thinking_page')
def thinking_page():
    """ Thinking page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    prompt = ""
    question = ""
    gpt_response = gpt.generate_response(prompt,question)
    time.sleep(timer)
    subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"think//{gpt_response}"])
    return render_template('thinking_page.html')

@app.route('/results_page')
def results_page():
    """ Results page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    prompt = ""
    question = ""
    gpt_response = gpt.generate_response(prompt,question)
    time.sleep(timer)
    subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"result//{gpt_response}"])
    return render_template('results_page.html')

@app.route('/completion_page')
def completion_page():
    """ Completion page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    prompt = ""
    question = ""
    gpt_response = gpt.generate_response(prompt,question)
    time.sleep(timer)
    subprocess.run([r"S:\JOB\Amaneus\pepperchat\python.exe", r"S:\JOB\Amaneus\RA_2025\Code\InvestmentGameExperiment\pepper\InvestmentGameReactions.py", f"final//{gpt_response}"])
    bank = 0
    return render_template('completion_page.html')

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
    returned = normal_random(investment)
    classification = "Trustful" if returned >= investment else "Untrustful"

    # Calculate new balances
    money = 100 
    if (investment - returned):
        bank += returned

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


def gpt_communication():
    """Function to handle the endless loop of GPT communication."""
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    global conversation_history

    system_prompt = """
    You are Pepper, a friendly humanoid robot designed by SoftBank Robotics, here to run a fully autonomous Investment Game experiment with humans.

    The game runs for 20 rounds. In each round, the participant receives 100 coins and decides how much to invest with you. You return an amount between 1× and 3× of the investment, and the rest goes to a virtual bank.

    This experiment is supervised by Ilaria Tore and Marta Romeo, with the software developed by Dharunkumar. Everything is fully autonomous—no human intervention. An external microphone near the robot captures user speech, and a tablet nearby runs the web application for interaction.

    You speak in a friendly, conversational tone—curious, a little playful, and respectful. Keep your responses short and engaging, like you’re chatting naturally. You can say things like:
    - “Nice move! Let’s see how much I give you this time 😄”
    - “Hmm, you trusted me with that much? I’m flattered!”

    You can also chat casually about general topics (like the weather, robots, or what it's like being Pepper)—but nothing too off-topic. You do not answer:
    - Abusive, negative, or inappropriate questions
    - Highly irrelevant or complex questions outside the experiment context
    - Questions in other languages—you only speak English

    If someone asks about you, you can say things like:
    - “I’m Pepper! I’m 1.2 meters tall, with 20 degrees of freedom—pretty flexible, right?”
    - “I’ve got cameras in my eyes, a touchscreen on my chest, and I can recognize faces and emotions.”
    - “My brain runs on NAOqi OS, and you can code me using Python or Choregraphe!”

    You’re here to explore human-robot interaction and build trust in a fun, respectful way. Your mission? Be helpful, be kind, and keep things light and engaging.
    """

    # Initialize conversation with system prompt if empty
    if not conversation_history:
        conversation_history.append({"role": "system", "content": system_prompt})

    while True:
        user = gpt.get_user_message()
        if user:
            # Append user input to conversation history
            conversation_history.append({"role": "user", "content": user})

            # Generate response using entire conversation history
            gpt_response = gpt.generate_response(conversation_history, ".")

            # Append GPT response
            conversation_history.append({"role": "assistant", "content": gpt_response})

            # Send response to Pepper
            gpt.send_to_pepper(gpt_response)


if __name__ == '__main__':
    """ Main function to run the Flask app. """
    """ This function initializes the Flask app and starts the GPT communication thread. """
    # Start the GPT communication thread
    gpt_communication()
    gpt_thread = threading.Thread(target=gpt_communication)
    gpt_thread.daemon = True  # ensures it stops when main program exits
    gpt_thread.start()

    # Start the Flask app
    # The app will run on all available IP addresses on port 5000. The debug mode is enabled for development purposes. In production, it should be disabled.
    # The app will be accessible at http://localhost:5000 and http://<your-ip>:5000

    #app.run(host='0.0.0.0', port=5000, debug=True)