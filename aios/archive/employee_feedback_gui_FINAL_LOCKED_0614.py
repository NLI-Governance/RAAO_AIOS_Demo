import streamlit as st
import speech_recognition as sr
import csv
from datetime import datetime

st.set_page_config(page_title="Employee Voice Panel", layout="centered")

st.markdown("## 🗣️ Employee Voice Panel")
st.markdown("Please share your thoughts, concerns, or ideas. Your voice matters.")

# === Feedback Input ===
if "feedback_input" not in st.session_state:
    st.session_state.feedback_input = ""

col1, col2 = st.columns([8, 1])
with col1:
    feedback_text = st.text_area(
        "💬 Your Feedback",
        value=st.session_state.feedback_input,
        placeholder="What would you like to say?",
        help="""You may:
- Suggest workplace improvements
- Report uncomfortable situations
- Ask for clarification
- Share ideas for the company
This space is for your voice—type freely or use the mic."""
    )

with col2:
    if st.button("🎤 Start Listening"):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                st.info("🎙️ Listening... speak now.")
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                st.session_state.feedback_input = text
                st.success("✅ Captured voice input.")
        except Exception as e:
            st.error(f"Mic error: {e}")

# === Category Selection ===
category = st.selectbox(
    "📁 Category",
    ["Workplace Environment", "Job Role / Duties", "Benefits / Compensation", "Other"],
    help="Select the area your feedback is related to."
)

# === Anonymity Checkbox ===
anonymous = st.checkbox("Submit anonymously", help="Your name will not be recorded.")

# === Submit Action ===
if st.button("✅ Submit Feedback"):
    if feedback_text.strip():
        with open("employee_feedback_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().isoformat(),
                category,
                "ANONYMOUS" if anonymous else "NAMED",
                feedback_text.strip()
            ])
        st.success("📝 Feedback submitted. Thank you for speaking up.")
        st.session_state.feedback_input = ""
    else:
        st.warning("⚠️ Feedback cannot be empty.")
