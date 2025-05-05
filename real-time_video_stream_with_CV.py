import streamlit as st
import cv2
import numpy as np
from datetime import datetime

# --- Streamlit UI ---
st.title("📷 Real-Time Video Stream with OpenCV")
st.sidebar.header("🎛️ Filter Settings")

# --- Sidebar: Canny Edge Filter Thresholds ---
low_thresh = st.sidebar.slider("Low Threshold", 0, 255, 50)
high_thresh = st.sidebar.slider("High Threshold", 0, 255, 150)
use_filter = st.sidebar.checkbox("Apply Canny Edge Filter", value=True)

# --- Snapshot Button ---
snapshot = st.sidebar.button("📸 Take Snapshot")

# --- Start Webcam Capture with DirectShow (Windows Fix) ---
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frame_display = st.empty()

if not cap.isOpened():
    st.error("❌ Unable to access webcam.")
else:
    ret, frame = cap.read()
    if not ret:
        st.warning("⚠️ Failed to grab frame.")
    else:
        # Process Frame: Apply Canny if selected
        if use_filter:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, low_thresh, high_thresh)
            display_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        else:
            display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display Frame
        frame_display.image(display_frame, channels="RGB")

        # Save Snapshot
        if snapshot:
            filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(filename, frame)
            st.success(f"✅ Snapshot saved as {filename}")

# Release the webcam when done
cap.release()
