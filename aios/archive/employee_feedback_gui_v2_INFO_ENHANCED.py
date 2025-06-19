import streamlit as st
import speech_recognition as sr
import csv
from datetime import datetime

st.set_page_config(page_title="Employee Voice Panel", layout="centered")

# Title
st.markdown("## 🗣️ Employee Voice Panel")
st.markdown("Please share your thoughts, concerns, or ideas. Your voice matters.")

# Feedback container
with st.form("feedback_form"):
    col1, col2 = st.columns([8, 1])

    with col1:
        feedback_text = st.text_area(
            "💬 Your Feedback",
            placeholder="What would you like to say?",
            key="feedback_input",
            help="""You may:
- Share a suggestion to improve your work environment
- Report something that made you feel uncomfortable or unsafe
- Ask for clarification about a task or policy
- Offer an idea for improving the company
Your feedback can be as short or long as needed. You may also speak your thoughts aloud using the mic button."""
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

    category = st.selectbox(
        "📁 Category",
        ["Workplace Environment", "Job Role / Duties", "Benefits / Compensation", "Other"],
        help="Choose the area your feedback relates to."
    )

    anonymous = st.checkbox("Submit anonymously", help="Check this box to leave feedback without attaching your name.")

    submitted = st.form_submit_button("✅ Submit Feedback")
    if submitted and feedback_text.strip():
        with open("employee_feedback_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().isoformat(),
                category,
                "ANONYMOUS" if anonymous else "NAMED",
                feedback_text.strip()
            ])
        st.success("📝 Feedback submitted. Thank you for your input.")
