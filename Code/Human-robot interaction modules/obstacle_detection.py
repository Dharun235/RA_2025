from naoqi import ALProxy

class ObstacleDetection:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.motion = ALProxy("ALMotion", ip, port)

    def enable_collision_avoidance(self):
        """Enables Pepper's collision avoidance."""
        self.motion.setCollisionProtectionEnabled("Move", True)

    def disable_collision_avoidance(self):
        """Disables Pepper's collision avoidance."""
        self.motion.setCollisionProtectionEnabled("Move", False)

    def get_collision_status(self):
        """Checks if collision protection is enabled."""
        return self.motion.getMoveConfig()
