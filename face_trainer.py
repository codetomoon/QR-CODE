import cv2
import os
import numpy as np

# Initialize the face detector and recognizer
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Pattern Histogram

# Prepare training data
dataset_folder = 'dataset'
image_paths = []
face_samples = []
labels = []

# Loop through the dataset folder to get the image paths
for subdir in os.listdir(dataset_folder):
    subfolder = os.path.join(dataset_folder, subdir)
    if os.path.isdir(subfolder):
        for filename in os.listdir(subfolder):
            if filename.endswith('.jpg'):
                image_path = os.path.join(subfolder, filename)
                image = cv2.imread(image_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
                
                # Detect faces in the image
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                
                for (x, y, w, h) in faces:
                    # Append face image and corresponding label
                    face_samples.append(gray[y:y+h, x:x+w])  # Cropped face
                    labels.append(int(subdir.split('_')[1]))  # User ID is embedded in the folder name

# Train the recognizer on the faces
recognizer.train(face_samples, np.array(labels))

# Save the trained model to a file
recognizer.save('face_recognizer.yml')

print("Model trained successfully and saved as 'face_recognizer.yml'")
