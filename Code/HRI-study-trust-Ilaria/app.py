from flask import Flask, render_template, request, jsonify
import subprocess
import random
import csv
import os
from flask_cors import CORS
import random
import numpy as np

bank = 0
app = Flask(__name__)
CORS(app)
PEPPER_MODE = False  # Set True when using Pepper
CSV_FILE = "data/results.csv"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# random number 
def normal_random(investment):
    # Define the range of possible return values
    max_return = 3 * (investment)
    min_return = 0
    
    # Define the midpoint of the range
    mid_point = (max_return) // 2

    
    # Set the standard deviation for the normal distribution
    # Standard deviation controls the spread. A smaller value gives a narrower peak, and a larger value gives a wider one.
    std_dev = max_return / 6  # This is a typical choice for normalization

    # Generate a random number from a normal distribution centered at mid_point
    value = np.random.normal(mid_point, std_dev)
    
    # Clip the value to ensure it's within the valid range [min_return, max_return]
    value = max(min_return, min(max_return, round(value)))
    
    return value

# Create CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Person ID", "Round", "Investment", "Returned", "Trustful", 'Person Money', 'Bank Money'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invest_page')
def invest_page():
    return render_template('invest_page.html')

@app.route('/thinking_page')
def thinking_page():
    return render_template('thinking_page.html')

@app.route('/results_page')
def results_page():
    return render_template('results_page.html')

@app.route('/completion_page')
def completion_page():
    bank = 0
    return render_template('completion_page.html')

@app.route('/invest', methods=['POST'])
def invest():
    global bank
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

    # chatgpt powered or not?
    gpt_powered = "yes"

    # Pepper mode activated
    if PEPPER_MODE:
        try:
            action = "trustful" if classification == "Trustful" else "untrustful"
            print(action)
            result = subprocess.run(
                ["S:\JOB\Amaneus\pepperchat\python.exe", "pepper-control.py", action],
                capture_output=True, text=True
            )
            if result.stdout:
                print(f"Pepper's response: {result.stdout.strip()}")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
        except Exception as e:
            print(f"Error running Pepper script: {e}")

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
    app.run(host='0.0.0.0', port=5000, debug=True)