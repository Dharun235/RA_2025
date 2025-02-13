from naoqi import ALProxy

class EmotionDetection:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.face_detection = ALProxy("ALFaceDetection", ip, port)
        self.memory = ALProxy("ALMemory", ip, port)

    def detect_face(self):
        """Returns True if a face is detected."""
        return self.memory.getData("FaceDetected") is not None

    def detect_emotion(self):
        """Returns detected emotion if available."""
        return self.memory.getData("ALBasicAwareness/HumanEmotions")
