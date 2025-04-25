from naoqi import ALProxy
import time

robot_ip = "127.0.0.1"
robot_port = 9559

motion = ALProxy("ALMotion", robot_ip, robot_port)
leds = ALProxy("ALLeds", robot_ip, robot_port)

# Set both face and ear LEDs to blue (indicating start)
leds.fadeRGB("FaceLeds", 0, 0, 1, 0.5)  # Blue for Face LEDs
leds.fadeRGB("EarLeds", 0, 0, 1, 0.5)   # Blue for Ear LEDs

# Move Pepper forward 1 meter
motion.moveTo(1, 0, 0)

# Wait for completion
time.sleep(2)

# Set both face and ear LEDs to green (indicating movement finished)
leds.fadeRGB("FaceLeds", 0, 1, 0, 0.5)  # Green for Face LEDs
leds.fadeRGB("EarLeds", 0, 1, 0, 0.5)   # Green for Ear LEDs
