import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Training Catalog Manager", layout="centered")
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=120)

st.markdown("### 🎓 Training Catalog Manager")
st.markdown("Add or update internal training modules available to employees.")

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

if not csv_path.exists():
    df_init = pd.DataFrame(columns=[
        "Training Name", "Training Type", "Trainer", "File Link", "Expiration Policy", "Notes"
    ])
    df_init.to_csv(csv_path, index=False)

# Form to add new training
with st.form("add_training_form"):
    col1, col2 = st.columns([3, 1])
    with col1:
        training_name = st.text_input("Training Name", help="Enter the official name of the training course.")
    with col2:
        training_type = st.selectbox("Training Type", ["Onboarding", "Compliance", "Skill", "Refresher", "Other"],
                                     help="Select the category this training belongs to.")

    trainer = st.text_input("Trainer", help="Enter the full name of the trainer or department responsible.")
    file_link = st.text_input("File Link (optional)", help="Paste a URL or file location for reference material.")
    expiration = st.text_input("Expiration Policy", help="e.g., Valid for 1 year, or 'None'")
    notes = st.text_area("Notes (optional)", help="Add extra details, prerequisites, or key takeaways.")

    submitted = st.form_submit_button("Add Training")
    if submitted:
        df = pd.read_csv(csv_path)
        new_row = pd.DataFrame([{
            "Training Name": training_name,
            "Training Type": training_type,
            "Trainer": trainer,
            "File Link": file_link,
            "Expiration Policy": expiration,
            "Notes": notes
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("✅ Training module added.")

# Show existing entries
st.markdown("### 📋 Current Training Modules")
df_existing = pd.read_csv(csv_path)
st.dataframe(df_existing, use_container_width=True)
