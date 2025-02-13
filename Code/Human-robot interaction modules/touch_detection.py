from naoqi import ALProxy

class TouchSensors:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.memory = ALProxy("ALMemory", ip, port)

    def is_head_touched(self):
        """Returns True if Pepper's head is touched."""
        return self.memory.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value") > 0

    def is_hand_touched(self, side="Left"):
        """Returns True if Pepper's hand is touched (Left/Right)."""
        key = f"Device/SubDeviceList/{side}Hand/Touch/Back/Sensor/Value"
        return self.memory.getData(key) > 0
