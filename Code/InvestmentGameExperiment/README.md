# Investment Game Experiment
This project sets up an autonomous Investment Game experiment involving a web interface, Gemini AI, and the Pepper robot.

## 📁 Project Structure

The project directory is organized as follows:

- **`InvestmentGameExperiment/`**
  - **`data/`**: Contains the CSV file `game.csv` which stores the values of various variables like participant ID, money, GPT-powered, etc and `conversation_log_intro.txt`, `conversation_log_game.txt` which contains the conversations between the user and gemini transcribed during the introduction and the game, respectively.
  - **`gpt/gpt_interface.py`**: Contains the scripts relevant to the conversation with Gemini AI model.
  - **`pepper/`**: Contains NAOQI-powered Python 2 scripts handling TTS and movement of the Pepper robot based on the current state.
  - **`static/`**: Contains JS and CSS files that manage the backend and styling of the web application.
  - **`templates/`**: Contains HTML files for different states of the game (start, investing, thinking, results, and final completion).
  - **`test/`**: Test folder for independent testing of modules.
  - **`web-app-loader`**: Electron based app to run the website as an app in full-screen kiosk mode.
  - **`utils`**: Functions used for general purposes across the code environment.
  - **`app.py`**: Main script containing the code for the flask based app and user-Gemini communication.
  - **`intro_ai.py`**: Script for ai based conversation during introduction.
  - **`intro_non_ai.py`**: Script for non-ai based conversation during introduction.
  - **`README.md`**: The main README file.
  - **`requirements_py3.txt`**: Requirements file for Python 3 dependencies.
  

## ⚙️ Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Dharun235/RA_2025.git
cd RA_2025/Code/InvestmentGameExperiment
```

### 2. Install Dependencies
Choose the appropriate Python version and follow the below instructions:

#### 👉 For Python 2:
Download NAOqi SDK from: http://doc.aldebaran.com/2-5/dev/python/install_guide.html

#### 👉 For Python 3:
Run the below command -

```bash
pip3 install -r requirements_py3.txt
```

### 3. Configure API and IP Address

#### Update Gemini API Key
In line 13 of gpt/gpt_interface.py, replace:

```bash
client = genai.Client(api_key="AIzaSyC3NHq1XSTbgtEcxo4w4in-toMicl4asig") # Replace with your actual API key
```

#### Update Pepper IP
Replace the ip address of Pepper robot in:

- Line 159 of pepper/InvestmentGameReactions.py

With your Pepper robot’s IP address:

```bash
PEPPER_IP = "xxx.xxx.x.xxx"  # Replace with your Pepper's IP address
```

### 4. Run the Application

- Connect to the same router as the pepper robot.

- For introduction conversation with non-ai setup, run the following commands
```bash
python intro_non_ai.py {Person_ID}
```
For example, if the participant ID is 1, the command is as follows 
```bash
python intro_non_ai.py 1
```

- For introduction conversation with ai setup, run the following commands
```bash
python intro_ai.py {Person_ID}
```
For example, if the participant ID is 1, the command is as follows 
```bash
python intro_ai.py 1
```

- For AI and Trustworthy condition, run the setup as below
```bash
python app.py yes T
```

- For AI and untrustworthy condition, run the setup as below
```bash
python app.py yes U
```

- For non-AI and Trustworthy condition, run the setup as below
```bash
python app.py not T
```

- For AI and untrustworthy condition, run the setup as below
```bash
python app.py not U
```

### 5. Open Web Interface

#### Run Electron App

- Due to size limitations, please download the full `web-app-loader` folder from this link:
https://drive.google.com/drive/folders/1EKmt6cJFKGBHKUP-uFWhS5jRvawCBC-D?usp=sharing 

- Place the `web-app-loader` into the root folder.
- Change the url of line 40 of web-app-loader/main.js to the url provided by the flask app. The line is given below.
    
```bash
mainWindow.loadURL('http://url-provided-by-flask-app');
```

- Then run the below commands in a seperate terminal:

```bash
cd web-app-loader
npm start
```

## Logging of data
You can check the conversations between "Participant" and "Pepper" in the following files- 
- data/conversation_log_game.txt - Conversations between "Participant" and "Pepper" during the game.
- data/conversation_log_intro.txt - Conversations between "Participant" and "Pepper" during the introduction.

You can check the various game related data such as bank amount, round number, etc in the data/game_data.csv.
## Maintainer

Dharunkumar Senthilkumar
(https://www.linkedin.com/in/dharun-kumar20/)
