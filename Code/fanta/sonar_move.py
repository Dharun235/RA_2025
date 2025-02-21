import qi
import time

ip = "127.0.0.1"
port = 9559

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + ip + ":" + str(port))

memory_service = session.service("ALMemory")
sonar_service = session.service("ALSonar")
motion_service = session.service("ALMotion")

# Enable sonar sensors
sonar_service.subscribe("myApplication")
time.sleep(1)  # Allow sensors to initialize

# Set Pepper to move continuously
motion_service.move(0.2, 0, 0)  # Move forward at 0.2 m/s

while True:
    front_distance = memory_service.getData("Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
    print("Front Distance:", front_distance)

    if front_distance < 1.0:  # If object is within 1 meter
        print("Obstacle detected! Stopping Pepper.")
        motion_service.stopMove()
        break  # Exit loop

    time.sleep(0.5)  # Reduce load on CPU

# Disable sonar sensors
sonar_service.unsubscribe("myApplication")
