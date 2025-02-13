from naoqi import ALProxy

class GestureDetection:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.tracker = ALProxy("ALTracker", ip, port)

    def track_hand(self):
        """Enables Pepper to track a user's hand movement."""
        self.tracker.registerTarget("Hand", [])
        self.tracker.track("Hand")

    def stop_tracking(self):
        """Stops tracking hand gestures."""
        self.tracker.stopTracker()
