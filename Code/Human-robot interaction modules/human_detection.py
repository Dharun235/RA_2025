from naoqi import ALProxy

class HumanDetection:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.people_perception = ALProxy("ALPeoplePerception", ip, port)
        self.tracker = ALProxy("ALTracker", ip, port)

    def enable_tracking(self):
        """Enables Pepper to track humans."""
        self.tracker.registerTarget("People", [])
        self.tracker.track("People")

    def disable_tracking(self):
        """Stops human tracking."""
        self.tracker.stopTracker()

    def get_detected_people(self):
        """Returns the number of detected people."""
        return self.people_perception.getData("PeoplePerception/PeopleDetected")
