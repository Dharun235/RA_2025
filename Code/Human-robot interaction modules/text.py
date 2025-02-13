import time
from tablet_display import TabletDisplay
from gesture_detection import GestureDetection
from emotion_detection import EmotionDetection
from touch_sensors import TouchSensors
from basic_movement import BasicMovement
from human_detection import HumanDetection
from speech import Speech
from obstacle_detection import ObstacleDetection

ROBOT_IP = "127.0.0.1"  # Change this to Pepper's IP if needed

def test_tablet():
    """Test displaying and hiding content on Pepper's tablet."""
    print("\n[TEST] Tablet Display Module")
    tablet = TabletDisplay(ip=ROBOT_IP)
    print("Displaying webpage...")
    tablet.show_web_page("https://www.google.com")
    time.sleep(5)
    print("Hiding webpage...")
    tablet.hide_web_page()
    print("[RESULT] Tablet test completed.\n")

def test_gesture():
    """Test Pepper's ability to track hand gestures."""
    print("\n[TEST] Gesture Detection Module")
    gesture = GestureDetection(ip=ROBOT_IP)
    print("Tracking hand... Move your hand near Pepper.")
    gesture.track_hand()
    time.sleep(5)
    gesture.stop_tracking()
    print("[RESULT] Gesture tracking stopped.\n")

def test_emotion():
    """Test Pepper's face and emotion detection."""
    print("\n[TEST] Emotion Detection Module")
    emotion = EmotionDetection(ip=ROBOT_IP)
    print("Checking for face detection...")
    face_detected = emotion.detect_face()
    if face_detected:
        print("[RESULT] Face detected!")
        emotion_type = emotion.detect_emotion()
        print("[RESULT] Detected Emotion:", emotion_type)
    else:
        print("[RESULT] No face detected.")
    print("[RESULT] Emotion test completed.\n")

def test_touch():
    """Test Pepper's touch sensors on head and hands."""
    print("\n[TEST] Touch Sensors Module")
    touch = TouchSensors(ip=ROBOT_IP)
    print("Touch Pepper's head or hands to test.")
    for i in range(10):  # Check for 10 seconds
        if touch.is_head_touched():
            print("[RESULT] Head touched!")
        if touch.is_hand_touched("Left"):
            print("[RESULT] Left hand touched!")
        if touch.is_hand_touched("Right"):
            print("[RESULT] Right hand touched!")
        time.sleep(1)
    print("[RESULT] Touch sensor test completed.\n")

def test_basic_movement():
    """Test basic robot movement (move forward and stop)."""
    print("\n[TEST] Basic Movement Module")
    movement = BasicMovement(ip=ROBOT_IP)
    print("Moving forward for 0.5 meters...")
    movement.move_forward(0.5)
    time.sleep(3)  # Let the robot move for 3 seconds
    movement.stop()
    print("[RESULT] Basic movement test completed.\n")

def test_human_detection():
    """Test human detection functionality."""
    print("\n[TEST] Human Detection Module")
    human_detector = HumanDetection(ip=ROBOT_IP)
    print("Checking for human presence...")
    detected = human_detector.detect_human()
    if detected:
        print("[RESULT] Human detected!")
    else:
        print("[RESULT] No human detected.")
    print("[RESULT] Human detection test completed.\n")

def test_speech():
    """Test speech functionality (Pepper speaks)."""
    print("\n[TEST] Speech Module")
    speech = Speech(ip=ROBOT_IP)
    print("Pepper will say 'Hello, I am Pepper!'")
    speech.say("Hello, I am Pepper!")
    time.sleep(2)  # Let the speech play
    print("[RESULT] Speech test completed.\n")

def test_obstacle_detection():
    """Test obstacle detection functionality."""
    print("\n[TEST] Obstacle Detection Module")
    obstacle = ObstacleDetection(ip=ROBOT_IP)
    print("Checking for obstacles in front of Pepper...")
    obstacle_detected = obstacle.detect_obstacle()
    if obstacle_detected:
        print("[RESULT] Obstacle detected!")
    else:
        print("[RESULT] No obstacle detected.")
    print("[RESULT] Obstacle detection test completed.\n")

if __name__ == "__main__":
    print("\n===== Running All Tests =====")
    test_tablet()
    test_gesture()
    test_emotion()
    test_touch()
    test_basic_movement()
    test_human_detection()
    test_speech()
    test_obstacle_detection()
    print("\n===== All Tests Completed Successfully =====")
