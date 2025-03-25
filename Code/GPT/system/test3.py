from naoqi import ALProxy
import time

# Set Pepper's IP
PEPPER_IP = "192.168.0.106"  # Replace with your Pepper's IP
PORT = 9559

# Connect to required proxies
motion = ALProxy("ALMotion", PEPPER_IP, PORT)
posture = ALProxy("ALRobotPosture", PEPPER_IP, PORT)
memory = ALProxy("ALMemory", PEPPER_IP, PORT)
people_perception = ALProxy("ALPeoplePerception", PEPPER_IP, PORT)
face_detection = ALProxy("ALFaceDetection", PEPPER_IP, PORT)
face_characteristics = ALProxy("ALFaceCharacteristics", PEPPER_IP, PORT)
gaze_analysis = ALProxy("ALGazeAnalysis", PEPPER_IP, PORT)
waving_detection = ALProxy("ALWavingDetection", PEPPER_IP, PORT)
sonar_service = ALProxy("ALSonar", PEPPER_IP, PORT)

# Enable services and configure the robot
people_perception.subscribe("PeopleTracking")
face_detection.subscribe("FaceDetection")
waving_detection.subscribe("WavingDetection")

motion.wakeUp()
posture.goToPosture("StandInit", 0.8)

# Human detection and characteristics
def detect_human():
    """Detect humans and analyze characteristics using ALPeoplePerception, ALFaceDetection, and ALFaceCharacteristics"""
    try:
        # Detect human faces and characteristics
        detected_faces = face_detection.getFaceInfo()
        if detected_faces:
            for face in detected_faces:
                print("Detected face ID:", face[0])
                face_features = face_characteristics.getFaceCharacteristics(face[0])
                print("Face features:", face_features)

        # Detect people using PeoplePerception
        people_ids = memory.getData("PeoplePerception/VisiblePeopleList")
        if people_ids:
            print(f"Detected people IDs: {people_ids}")
            for person_id in people_ids:
                # Get person's position in robot frame
                position = memory.getData(f"PeoplePerception/Person/{person_id}/PositionInRobotFrame")
                print(f"Person {person_id} position (x, y, z): {position}")

        # Detect if anyone is waving
        waving = waving_detection.isWaving()
        if waving:
            print("A person is waving!")

    except Exception as e:
        print("Error in detecting humans or analyzing faces:", e)

def detect_obstacles():
    """Detect obstacles using sonar sensors"""
    try:
        left_dist = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        right_dist = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        front_dist = memory.getData("Device/SubDeviceList/US/Front/Sensor/Value")
        return left_dist, right_dist, front_dist
    except Exception as e:
        print("Error in sonar detection:", e)
        return None, None, None

def obstacle_avoidance():
    """Implement obstacle avoidance logic for Pepper using sonar"""
    left_dist, right_dist, front_dist = detect_obstacles()

    if left_dist < 0.5:  # Obstacle detected on the left
        print("Obstacle detected on the left! Turning right.")
        motion.moveTo(0.3, 0.0, -0.5)  # Turn right
    elif right_dist < 0.5:  # Obstacle detected on the right
        print("Obstacle detected on the right! Turning left.")
        motion.moveTo(0.3, 0.0, 0.5)  # Turn left
    elif front_dist < 0.5:  # Obstacle detected in front
        print("Obstacle detected in front! Moving backward.")
        motion.moveTo(-0.3, 0.0, 0.0)  # Move backward

def move_to_human():
    """Move the robot to the detected human"""
    closest_person = memory.getData("PeoplePerception/ClosestPerson")
    if closest_person:
        position = memory.getData(f"PeoplePerception/Person/{closest_person}/PositionInRobotFrame")
        if position:
            print(f"Moving toward person at position: {position}")
            x, y, z = position
            motion.moveTo(x * 0.5, y * 0.5, 0)  # Move toward the person
        else:
            print("No position data for closest person.")
    else:
        print("No human detected to move towards.")

def main_loop():
    """Main loop to continuously track people, detect obstacles, and respond to sound"""
    while True:
        try:
            # Detect human faces, characteristics, and waving
            detect_human()

            # Detect and avoid obstacles
            obstacle_avoidance()

            # Move toward the closest detected person
            move_to_human()

            # Pause for a moment before next iteration
            time.sleep(1)

        except KeyboardInterrupt:
            print("Interrupted by user.")
            break

if __name__ == "__main__":
    main_loop()
