import time
from naoqi import ALProxy
import sys
import termios
import tty

# Initialize proxies
motion = ALProxy("ALMotion", "127.0.0.1", 9559)
motion.setStiffnesses("Body", 1.0)

# Setup movement parameters
linear_speed = 0.1  # m/s
angular_speed = 0.3  # rad/s

def move_forward():
    motion.moveToward(linear_speed, 0, 0)

def move_backward():
    motion.moveToward(-linear_speed, 0, 0)

def turn_left():
    motion.moveToward(0, 0, angular_speed)

def turn_right():
    motion.moveToward(0, 0, -angular_speed)

def stop():
    motion.moveToward(0, 0, 0)

# Get a single key press without needing to hit enter
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Main loop for real-time control
while True:
    key = get_key()  # Get the key pressed

    if key == 'w':
        move_forward()
    elif key == 's':
        move_backward()
    elif key == 'a':
        turn_left()
    elif key == 'd':
        turn_right()
    elif key == 'q':  # Quit the program
        stop()
        break
    else:
        stop()

    time.sleep(0.05)  # Delay for smoother movement and to reduce CPU load
