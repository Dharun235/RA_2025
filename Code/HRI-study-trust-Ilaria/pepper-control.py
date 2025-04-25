#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from naoqi import ALProxy

PEPPER_IP = "192.168.0.108"  # Change to your Pepper's IP
PEPPER_PORT = 9559

def control_pepper(action):
    try:
        leds = ALProxy("ALLeds", PEPPER_IP, PEPPER_PORT)
        motion = ALProxy("ALMotion", PEPPER_IP, PEPPER_PORT)
        tts = ALProxy("ALTextToSpeech", PEPPER_IP, PEPPER_PORT)
        if action == "trustful":
            leds.fadeRGB("EarLeds", 0, 1, 0, 0.5)   # Green LEDs
            motion.openHand("RHand")  # Open hand
            #tts.say("Thank you for trusting me!")
        elif action == "untrustful":
            leds.fadeRGB("EarLeds", 0, 0, 1, 0.5)  # Blue LEDs
            motion.closeHand("RHand")  # Close hand
            #tts.say("Oh, I am sorry! Maybe next time?")
    except Exception as e:
        print("Error:", e)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: S:\JOB\Amaneus\pepperchat\python.exe pepper-control.py <trustful/untrustful>")
    else:
        control_pepper(sys.argv[1])
