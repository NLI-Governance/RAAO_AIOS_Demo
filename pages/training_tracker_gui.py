import streamlit as st
from components.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_language_toggle,
    display_about_section,
    display_chatgpt_assistant
)

st.set_page_config(page_title="Training Tracker", layout="wide")
display_logo()
display_language_toggle()
display_about_section("Use this form to log employee training completions. Each record is stored for compliance reporting.")

st.markdown("### 📋 Training Tracker")
st.info("Fill out the training completion form below.")

col1, col2 = st.columns(2)
with col1:
    employee_name = st.text_input("Employee Name 🛈", placeholder="Start typing...")
    training_title = st.selectbox("Training Title 🛈", ["OSHA 10", "CPR Certification", "Cybersecurity Awareness"])
    completion_date = st.date_input("Completion Date 🛈")
with col2:
    trainer_name = st.text_input("Trainer Name 🛈")
    training_hours = st.number_input("Training Hours 🛈", min_value=0.0, format="%.1f")
    certification_received = st.checkbox("Certification Received 🛈")

if st.button("Submit Training Record"):
    st.success("✅ Training record submitted successfully!")

display_chatgpt_assistant()
display_abl_footer()

st.markdown("`training_tracker_gui.py`")