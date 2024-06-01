import streamlit as st
import vehicle_detection
import tempfile

def main():
    st.title("Vehicle Detection App")

    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"])
    if uploaded_video is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_video.read())
            temp_video_path = tmp_file.name
        vehicle_detection.detect_vehicles(temp_video_path)

if __name__ == "__main__":
    main()
