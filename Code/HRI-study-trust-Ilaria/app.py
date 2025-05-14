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
    gpt_response = gpt.generate_response("","")
    time.sleep(timer)
    subprocess.run(["S:\JOB\Amaneus\pepperchat\python.exe", "S:\JOB\Amaneus\RA_2025\Code\HRI-study-trust-Ilaria\pepper\InvestmentGameReactions.py", f"start//{gpt_response}"])
    return render_template('index.html')

@app.route('/invest_page')
def invest_page():
    """ Investment page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    gpt_response = gpt.generate_response("","")
    time.sleep(timer)
    subprocess.run(["S:\JOB\Amaneus\pepperchat\python.exe", "S:\JOB\Amaneus\RA_2025\Code\HRI-study-trust-Ilaria\pepper\InvestmentGameReactions.py", f"invest//{gpt_response}"])
    return render_template('invest_page.html')

@app.route('/thinking_page')
def thinking_page():
    """ Thinking page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    gpt_response = gpt.generate_response("","")
    time.sleep(timer)
    subprocess.run(["S:\JOB\Amaneus\pepperchat\python.exe", "S:\JOB\Amaneus\RA_2025\Code\HRI-study-trust-Ilaria\pepper\InvestmentGameReactions.py", f"think//{gpt_response}"])
    return render_template('thinking_page.html')

@app.route('/results_page')
def results_page():
    """ Results page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    gpt_response = gpt.generate_response("","")
    time.sleep(timer)
    subprocess.run(["S:\JOB\Amaneus\pepperchat\python.exe", "S:\JOB\Amaneus\RA_2025\Code\HRI-study-trust-Ilaria\pepper\InvestmentGameReactions.py", f"result//{gpt_response}"])
    return render_template('results_page.html')

@app.route('/completion_page')
def completion_page():
    """ Completion page of the app. """
    global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
    gpt_response = gpt.generate_response("","")
    time.sleep(timer)
    subprocess.run(["S:\JOB\Amaneus\pepperchat\python.exe", "S:\JOB\Amaneus\RA_2025\Code\HRI-study-trust-Ilaria\pepper\InvestmentGameReactions.py", f"final//{gpt_response}"])
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
    """ This function runs in a separate thread to handle communication with the GPT model. """
    while True:
        global bank, person_id, round_num, investment, returned, classification, money, gpt_powered
        prompt = ""
        user = gpt.get_user_message()
        if user:
            gpt_response = gpt.generate_response(prompt, user)
            gpt.send_to_pepper(gpt_response)


if __name__ == '__main__':
    """ Main function to run the Flask app. """
    """ This function initializes the Flask app and starts the GPT communication thread. """
    # Start the GPT communication thread
    gpt_thread = threading.Thread(target=gpt_communication)
    gpt_thread.daemon = True  # ensures it stops when main program exits
    gpt_thread.start()

    # Start the Flask app
    # The app will run on all available IP addresses on port 5000. The debug mode is enabled for development purposes. In production, it should be disabled.
    # The app will be accessible at http://localhost:5000 and http://<your-ip>:5000

    app.run(host='0.0.0.0', port=5000, debug=True)