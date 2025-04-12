import cv2
import os
import datetime

# Initialize the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create dataset folder if not exists
dataset_folder = 'dataset'
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# Get user information for name and ID
user_id = input("Enter your ID: ")
name = input("Enter your name: ")

# Open the user text file for writing the user data
user_text_file = 'user_text.txt'

# Save user info to the text file with date and time
with open(user_text_file, 'a') as file:
    file.write(f"ID: {user_id}, Name: {name}, Date: {datetime.datetime.now()}\n")

print(f"User data saved! Capturing images for {name}...")

# Capture 30 images for the dataset
count = 0
while count < 30:
    ret, frame = cap.read()  # Capture a frame
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Resize the frame to speed up detection
    frame_resized = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Process each face found
    for (x, y, w, h) in faces:
        count += 1
        # Save the face image
        cv2.imwrite(f"{dataset_folder}/User.{user_id}.{count}.jpg", frame_resized[y:y+h, x:x+w])
        
        # Draw rectangle around the face
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the frame
    cv2.imshow('Capturing', frame_resized)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Images for {name} captured successfully!")
