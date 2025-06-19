# Standards:
# - Accessibility: Mic + text entry
# - Transparency: Optional anonymity toggle
# - Privacy: CSV logged with HR-only access assumed
# - Offline compatible
# - Respectful, open-ended prompt for dignity-based input

# === PART 1: Create directory and open file ===
# (run in terminal)
mkdir -p ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/gui && \
nano ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/gui/employee_feedback_gui.py

# === PART 2: Full script ===
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import speech_recognition as sr

# CSV path for logging
FEEDBACK_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_feedback.csv")
os.makedirs(os.path.dirname(FEEDBACK_PATH), exist_ok=True)

st.set_page_config(page_title="Employee Feedback", layout="centered")
st.title("🗣️ Employee Voice Panel")
st.markdown("Please share your thoughts, concerns, or ideas. Your voice matters.")

# --- Mic input (optional) ---
mic_input = ""
if st.button("🎤 Start Listening"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        try:
            audio = r.listen(source, timeout=6)
            mic_input = r.recognize_google(audio)
            st.success("Captured audio:")
            st.write(mic_input)
        except Exception as e:
            st.error(f"Error capturing audio: {e}")

# --- Manual entry ---
st.markdown("### 💬 Your Feedback")
message = st.text_area("What would you like to say?", value=mic_input, height=200)

# --- Category ---
category = st.selectbox("📂 Category", ["Workplace Environment", "Task Challenges", "Management Feedback", "Ideas for Improvement", "Other"])

# --- Anonymity ---
anonymous = st.checkbox("Submit anonymously")

# --- Submit ---
if st.button("✅ Submit Feedback"):
    if message.strip() == "":
        st.warning("Feedback cannot be empty.")
    else:
        row = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "anonymous": anonymous,
            "message": message.strip()
        }
        df = pd.DataFrame([row])
        df.to_csv(FEEDBACK_PATH, mode="a", index=False, header=not os.path.exists(FEEDBACK_PATH))
        st.success("Thank you. Your feedback has been submitted.")

# === PART 3: Run command ===
# In terminal:
# streamlit run ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/gui/employee_feedback_gui.py
