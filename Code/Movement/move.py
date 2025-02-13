from naoqi import ALProxy

# Connect to motion proxy
motion = ALProxy("ALMotion", "127.0.0.1", 9559)

# Wake up Pepper (if needed)
motion.wakeUp()

# Move forward (0.5m)
distance = 0.5  # Meters
speed = 0.2  # Adjust speed (0.2 m/s is reasonable)

motion.moveTo(distance, 0, 0)  # (x, y, theta) - Move forward only

# Stop movement (optional, just for safety)
motion.stopMove()

# Rest position (optional)
motion.rest()
