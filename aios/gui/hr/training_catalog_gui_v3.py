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

# Reusable info icon
def info(label, tip):
    st.markdown(
        f"<div style='display:flex; align-items:center;'>"
        f"<span>{label}</span>"
        f"<span title='{tip}' style='margin-left:5px;color:#555;font-size:18px;cursor:help;'>❓</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# Load existing or create new
if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Training Name", "Training Type", "Trainer",
        "Duration (hrs)", "Renewal Period", "Description", "Filename"
    ])

with st.form("add_training"):
    st.subheader("➕ Add New Training")

    info("Training Name", "Official title of the training module.")
    name = st.text_input("")

    info("Training Type", "Choose the general category of the training.")
    t_type = st.selectbox("", ["Onboarding", "Safety", "Compliance", "Job-Specific", "Other"])

    info("Trainer", "Name of the trainer, organization, or source.")
    trainer = st.text_input("")

    info("Duration (hrs)", "Total expected completion time in hours.")
    duration = st.number_input("", min_value=0.5, step=0.5)

    info("Renewal Period", "How often the training must be repeated (e.g., Annual).")
    renewal = st.text_input("")

    info("Description", "Brief summary of training content or objectives.")
    desc = st.text_area("", height=100)

    info("Upload Training File", "Accepted formats: PDF, MP4, or DOCX.")
    uploaded_file = st.file_uploader("", type=["pdf", "mp4", "docx"])

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
        st.success("✅ Training module added.")

# View
st.divider()
st.subheader("📋 Current Training Catalog")
st.dataframe(df, use_container_width=True)
