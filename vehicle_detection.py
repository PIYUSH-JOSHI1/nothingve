import cv2
import numpy as np
import streamlit as st

# Specify the full path to the Haar cascade XML file
CASCADE_XML_PATH = "path/to/haarcascade_car.xml"

# Load pre-trained vehicle detection model (Haar Cascade)
vehicle_cascade = cv2.CascadeClassifier(CASCADE_XML_PATH)

def detect_vehicles(video_file):
    cap = cv2.VideoCapture(video_file)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 1)

        # Draw rectangles around detected vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Convert the frame to RGB format for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame, channels="RGB", use_column_width=True)

    cap.release()
