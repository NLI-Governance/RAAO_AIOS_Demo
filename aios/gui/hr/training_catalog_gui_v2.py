import streamlit as st
import pandas as pd
from pathlib import Path

# Paths
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv").expanduser()
upload_dir = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/training_modules").expanduser()
logo_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()
upload_dir.mkdir(parents=True, exist_ok=True)

# Logo
if logo_path.exists():
    st.image(str(logo_path), width=100)

st.title("🎓 Training Catalog Manager")

# Standard info icon using hover
def info_icon(label, tooltip):
    st.markdown(
        f"<span style='display:inline-block'>{label} "
        f"<span title='{tooltip}' style='color:#999;font-size:18px;cursor:help;'>❓</span></span>",
        unsafe_allow_html=True,
    )

# Load or create data
if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Training Name", "Training Type", "Trainer",
        "Duration (hrs)", "Renewal Period", "Description", "Filename"
    ])

with st.form("add_training"):
    st.subheader("➕ Add New Training")

    name = st.text_input("Training Name")
    info_icon("Training Name", "This is the official title of the training module.")

    t_type = st.selectbox("Training Type", ["Onboarding", "Safety", "Compliance", "Job-Specific", "Other"])
    info_icon("Training Type", "Select the category that best fits the training purpose.")

    trainer = st.text_input("Trainer / Provider Name")
    info_icon("Trainer", "Who is leading or providing this training?")

    duration = st.number_input("Duration (hrs)", min_value=0.5, step=0.5)
    info_icon("Duration", "Expected time to complete the training.")

    renewal = st.text_input("Renewal Period (e.g., Annual, Bi-Annual)")
    info_icon("Renewal Period", "Indicate how often this training must be retaken.")

    desc = st.text_area("Description", height=100)
    info_icon("Description", "Brief description of the training content or purpose.")

    uploaded_file = st.file_uploader("Upload Training Module", type=["pdf", "mp4", "docx"])
    info_icon("Upload", "Upload the actual training material file (PDF, DOCX, or MP4).")

    submitted = st.form_submit_button("Save Training")

    if submitted and name:
        filename = ""
        if uploaded_file:
            file_path = upload_dir / uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())
            filename = uploaded_file.name

        new_row = {
            "Training Name": name,
            "Training Type": t_type,
            "Trainer": trainer,
            "Duration (hrs)": duration,
            "Renewal Period": renewal,
            "Description": desc,
            "Filename": filename
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("✅ Training module added successfully!")

# View catalog
st.divider()
st.subheader("📋 Current Training Catalog")
st.dataframe(df, use_container_width=True)
