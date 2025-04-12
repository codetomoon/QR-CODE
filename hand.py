import cv2
import mediapipe as mp
import pyautogui
import time
from pynput.keyboard import Controller
from math import dist

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start the webcam capture
cap = cv2.VideoCapture(0)

# Initialize the last gesture state to avoid repeated volume control actions
last_gesture = None
last_time = time.time()

# Initialize pynput keyboard controller
keyboard = Controller()

# Function to control volume with pynput (press volume keys)
def control_volume(action):
    if action == "volume_up":
        # Press 'volume up' key
        keyboard.press('volume up')
        keyboard.release('volume up')
    elif action == "volume_down":
        # Press 'volume down' key
        keyboard.press('volume down')
        keyboard.release('volume down')

# Function to take a screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshots.png')  # Save to a fixed file
    print("Screenshot saved as screenshots.png!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Flip the frame horizontally for a later mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB (required for MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and find hands
    results = hands.process(rgb_frame)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw the landmarks on the hand
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract thumb tip, index finger tip, and wrist landmarks
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_cmc = landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]  # Thumb base
            wrist = landmarks.landmark[mp_hands.HandLandmark.WRIST]  # Wrist base

            # Calculate the distance between thumb base and thumb tip (length of thumb)
            thumb_length = dist((thumb_cmc.x, thumb_cmc.y), (thumb_tip.x, thumb_tip.y))

            # Calculate the angle between thumb and index (this can help detect the gunpoint gesture)
            thumb_angle = (thumb_tip.x - thumb_cmc.x) * (index_tip.y - thumb_cmc.y) - (thumb_tip.y - thumb_cmc.y) * (index_tip.x - thumb_cmc.x)
            thumb_angle = abs(thumb_angle)

            # Threshold for recognizing gunpoint gesture (angle and thumb length)
            if thumb_angle > 0.01 and thumb_length > 0.1:  # Threshold values might need adjustment
                current_gesture = "gunpoint"
            else:
                current_gesture = None

            # Perform volume control action or screenshot based on gesture
            if current_gesture != last_gesture and time.time() - last_time > 1:  # 1-second debounce
                if current_gesture == "gunpoint":
                    print("Gunpoint gesture detected - Taking Screenshot")
                    take_screenshot()
                elif current_gesture == "thumb_up":
                    print("Thumb and index extended - Volume Up")
                    control_volume("volume_up")
                elif current_gesture == "pinch":
                    print("Thumb and index pinch - Volume Down")
                    control_volume("volume_down")

                # Update last gesture and time
                last_gesture = current_gesture
                last_time = time.time()

    # Display the frame with hand landmarks
    cv2.imshow("Hand Gesture Volume Control and Screenshot System", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
