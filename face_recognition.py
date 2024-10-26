# Import required libraries
import dlib
import cv2
import numpy as np

# Initialize dlib's face detector (HOG-based)
face_detector = dlib.get_frontal_face_detector()

# Function for performing face detection
def perform_face_recognition():
    # Open a connection to the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale (face detector works better in grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_detector(gray)

        # Loop through each face detected
        for face in faces:
            # Get the coordinates of the rectangle that bounds the face
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame with face bounding boxes
        cv2.imshow('Face Recognition', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

# Main execution
if __name__ == "__main__":
    perform_face_recognition()
