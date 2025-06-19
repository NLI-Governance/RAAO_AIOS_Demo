import streamlit as st
import pandas as pd
from pathlib import Path

# Constants
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv").expanduser()
logo_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()

# Logo
if logo_path.exists():
    st.image(str(logo_path), width=100)

st.title("📘 Training Catalog Manager")

# Info icon helper
def info_icon(text):
    st.markdown(f":grey_question: <span title='{text}'>ℹ️</span>", unsafe_allow_html=True)

# Load or create DataFrame
if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Training Name", "Training Type", "Trainer", "Duration (hrs)", "Renewal Period", "Description"
    ])

with st.form("add_training"):
    st.subheader("➕ Add a New Training Entry")

    name = st.text_input("Training Name")
    info_icon("The title of the training module")

    t_type = st.selectbox("Training Type", ["Onboarding", "Safety", "Compliance", "Job-Specific", "Other"])
    info_icon("Categorize the training")

    trainer = st.text_input("Trainer or Provider Name")
    duration = st.number_input("Duration (hrs)", min_value=0.5, step=0.5)
    renewal = st.text_input("Renewal Period (e.g. Annual, Bi-Annual)")
    desc = st.text_area("Description", height=100)

    submitted = st.form_submit_button("Add Training")

    if submitted and name:
        new_row = {
            "Training Name": name,
            "Training Type": t_type,
            "Trainer": trainer,
            "Duration (hrs)": duration,
            "Renewal Period": renewal,
            "Description": desc
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("✅ Training entry added successfully!")

# Display current catalog
st.divider()
st.subheader("📋 Current Training Catalog")
st.dataframe(df, use_container_width=True)
