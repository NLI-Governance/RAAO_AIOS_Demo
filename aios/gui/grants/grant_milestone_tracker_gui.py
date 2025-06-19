import streamlit as st
import pandas as pd
from pathlib import Path

# Logo
logo_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()
st.image(str(logo_path), width=100)

st.markdown("## 📌 Grant Milestone Tracker")
st.markdown("Track major milestones and deadlines tied to specific grants.")

# Load grant codes
code_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv").expanduser()
if not code_path.exists():
    st.error("Grant codes CSV not found.")
    st.stop()

codes_df = pd.read_csv(code_path)
grant_codes = sorted(codes_df["Grant Code"].dropna().unique().tolist())

# UI Form
with st.form("milestone_form"):
    col1, col2 = st.columns(2)

    with col1:
        selected_grant_code = st.selectbox(
            "Grant Code ℹ️", grant_codes,
            help="Select the grant this milestone is tied to."
        )
    with col2:
        milestone_title = st.text_input(
            "Milestone Title ℹ️",
            help="Name of the milestone (e.g., Monthly Report Due)"
        )

    milestone_date = st.date_input("Milestone Date ℹ️", help="Date by which the milestone must be completed.")
    responsible_party = st.text_input("Responsible Staff ℹ️", help="Name of the staff member accountable for this milestone.")
    status = st.selectbox("Status ℹ️", ["Pending", "In Progress", "Completed"], help="Track progress of the milestone.")
    notes = st.text_area("Additional Notes ℹ️", help="Optional space to include context or follow-up info.")

    submitted = st.form_submit_button("Log Milestone")

# Save to CSV
log_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_milestones_log.csv").expanduser()

if submitted:
    entry = {
        "Grant Code": selected_grant_code,
        "Milestone Title": milestone_title,
        "Milestone Date": milestone_date.strftime("%Y-%m-%d"),
        "Responsible Party": responsible_party,
        "Status": status,
        "Notes": notes
    }

    if log_path.exists():
        existing_df = pd.read_csv(log_path)
        new_df = pd.concat([existing_df, pd.DataFrame([entry])], ignore_index=True)
    else:
        new_df = pd.DataFrame([entry])

    new_df.to_csv(log_path, index=False)
    st.success("✅ Milestone successfully logged.")
