# Investment Game Experiment Code 
This repository contains necessary codes for the experiment - Investment Game Experiment. 

## 📖 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Directory Structure](#-project-structure)
    - [Clone the repository](#1️⃣-clone-the-repository)
    - [Navigate to the Project Directory](#2️⃣-navigate-to-the-project-directory)
    - [Install Dependencies](#-install-dependencies)
    - [Update API key and IP address](#-update-api-key-and-pepper-ip-address)
    - [Run the application](#-run-the-application)
- [Setup and Usage](#️-setup)
- [Contact](#contact)

## 📘 About

Brief explanation of what your project does and why it's useful.

## ✨ Features

- ✅ Web based interface 
- ✅ Fully autonomous system
- ✅ Gemini AI for communication

## 🧰 Tech Stack

- Python 2 and Python 3
- Naoqi
- Model - gemini-2.0-flash

## 📂 Project Structure
HRI-study-trust-Ilaria/
├── data/ # Contains csv file results.csv which stores the values of various variables such as participant id, money, gpt-powered, etc
├── gpt/ # Contains the scripts relevant to Gemini AI model
├── pepper/ # Contains NAOQI powered python 2 scripts handling the tts and movement of pepper robot in accordance to the current state
├── static/ # Contains js and css files handling the backend and style of the web application
├── templates/ # Contains html files of different states of the game - start, investing, thinking, results and final completion
├── test/ # Test folder which can be used for independent testing of modules
├── requirements_py2.txt # Requirements file for python 3 dependencies
├── requirements_py3.txt # Requirements file for python 3 dependencies
├── app.py # Overall app handling both web application and user gemini communication. 
└── README.md # The main README file

## ⚙️ Setup and Usage

### 1️⃣ Clone the Repository
Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Dharun235/RA_2025/tree/main/Code/HRI-study-trust-Ilaria
```

### 2️⃣ Navigate to the Project Directory
Change to the project directory:

```
bash
cd HRI-study-trust-Ilaria
```

### 📦 Install Dependencies
Choose the appropriate Python version and run the corresponding command:

#### 👉 For Python 2:

```
bash
pip2 install -r requirements_py2.txt
```

#### 👉 For Python 3:

```
bash
pip3 install -r requirements_py3.txt
```

### 🔑 Update API Key and Pepper IP Address
Before running the project, you must update the API key and Pepper robot's IP address in the relevant scripts.

#### 1️⃣ Change the API Key
Open the gpt/gpt_interface.py file and locate the line where the API key is defined. Replace the placeholder with your actual API key:

```
python
client = genai.Client(api_key="YOUR_API_KEY_HERE")  # Replace with your actual API key
```

#### 2️⃣ Update Pepper Robot's IP Address
Similarly, find and update the Pepper robot's IP address in the following scripts:
● pepper/InvestmentGameReactions.py
● pepper/speak.py
Replace the placeholder with your Pepper robot's IP address:

```
python
PEPPER_IP = "192.168.1.108"  # Replace with your Pepper's IP address
```

### 🚀 Run the Application
Once you have completed the setup, you can run the application:

```
bash
python app.py
```

## Contact
Created by [Dharunkumar Senthilkumar](https://www.linkedin.com/in/dharun-kumar20/) - feel free to contact me!