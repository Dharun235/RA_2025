from naoqi import ALProxy

class Speech:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.tts = ALProxy("ALTextToSpeech", ip, port)

    def say(self, text):
        """Makes Pepper speak the given text."""
        self.tts.say(text)
