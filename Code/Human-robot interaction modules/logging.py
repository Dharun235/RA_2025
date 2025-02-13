from naoqi import ALProxy
import time

class Logger:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.memory = ALProxy("ALMemory", ip, port)

    def get_sonar_data(self):
        """Gets sonar sensor readings."""
        left = self.memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        right = self.memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        return {"left_sonar": left, "right_sonar": right}

    def log_data(self, filename="pepper_log.txt"):
        """Logs sensor data to a file."""
        with open(filename, "a") as file:
            data = self.get_sonar_data()
            file.write(f"{time.time()}: {data}\n")
