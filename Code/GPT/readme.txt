# DialoGPT-Pepper Chatbot Integration

This project integrates **DialoGPT (running on a PC) with the SoftBank Pepper Robot** to enable conversational AI.

## 🛠 Setup Steps

### 1️⃣ Install Dependencies  
#### On PC (Python 3)
```sh
pip install transformers torch flask requests

#### On Pepper (Python 2)
```sh
pip install requests

### 2️⃣ Run the DialoGPT Server on PC
```sh
python dialogpt_server.py

### 3️⃣ Configure Pepper to Connect to project
Change the IP address to your PC's IP inside the file - client_test.py line 6
````sh
DIALOGPT_SERVER_IP = "192.168.0.101" 

### 4️⃣ Run the Pepper Client
1. Store the code client_test.py in pepper robot. 
````sh 
python pepper_chat.py
2. If you have installed dependencies of naoqi and python2.7 in your local pc, you can change the pepper IP in line 10 of client_test.py.
````sh
PEPPER_IP = "127.0.0.1" 

##💡 How It Works
1. Pepper captures user speech and sends it to DialoGPT (running on PC).
2. DialoGPT generates a response and sends it back.
3. Pepper speaks the response.

## 🛠 Troubleshooting
1. Connection Issues?
a. Check the IP address of your PC (ipconfig on Windows or ifconfig on Linux/Mac).
b. Ensure both PC and Pepper are on the same network.

2. Errors on Pepper?
a. Ensure Python 2 is used on Pepper.
b. Install requests (pip install requests).

3. Errors on PC?
a. Run the server in Python 3.
b. Check if Flask API is running (http://192.168.0.101:5000/chat).

## 🚀 Future Improvements
1. Use a local LLM to avoid internet dependency.
2. Improve speech recognition and response time.

📌 Author: Dharunkumar Senthilkumar
📌 License: MIT