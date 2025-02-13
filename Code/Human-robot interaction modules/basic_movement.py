from naoqi import ALProxy

class MotionControl:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.motion = ALProxy("ALMotion", ip, port)
        self.motion.wakeUp()

    def move_forward(self, distance=0.5, speed=0.2):
        """Moves Pepper forward by a given distance (meters)."""
        self.motion.moveTo(distance, 0, 0)

    def turn(self, angle):
        """Rotates Pepper by a given angle (radians)."""
        self.motion.moveTo(0, 0, angle)

    def stop(self):
        """Stops Pepper's movement."""
        self.motion.stopMove()

    def rest(self):
        """Puts Pepper in rest mode."""
        self.motion.rest()
