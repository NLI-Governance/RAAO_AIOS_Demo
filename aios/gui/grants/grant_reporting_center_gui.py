import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

logo_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"
st.image(str(logo_path), width=120)
st.title("📄 Grant Reporting Center")
st.caption("Compile and submit required reports for grant compliance and funder review.")

# Load grant names
codes_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv"
codes_df = pd.read_csv(codes_path)
grant_names = sorted(codes_df["Grant Code"].dropna().unique().tolist())

with st.form("report_form"):
    grant = st.selectbox("Select Grant Code", grant_names)
    report_type = st.selectbox("Report Type", ["Quarterly", "Annual", "Custom"])
    report_period = st.date_input("Report Period End Date", value=date.today())

    st.markdown("### Summary Metrics")
    total_spent = st.number_input("Total Funds Spent", min_value=0.0, step=100.0)
    individuals_served = st.number_input("Individuals Reached", min_value=0, step=1)
    hours_logged = st.number_input("Total Staff Hours", min_value=0.0, step=1.0)

    st.markdown("### Narrative Sections")
    outcomes = st.text_area("Summary of Outcomes Achieved")
    barriers = st.text_area("Barriers Encountered")
    plan = st.text_area("Plans for Next Period")

    uploaded_file = st.file_uploader("Attach Report Document (optional)", type=["pdf", "docx", "jpg"])

    submitted = st.form_submit_button("Submit Grant Report")

    if submitted:
        log_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_reports.csv"
        log_exists = log_path.exists()

        if log_exists:
            log_df = pd.read_csv(log_path)
        else:
            log_df = pd.DataFrame(columns=[
                "Grant Code", "Report Type", "Period End", "Spent", "Served", "Hours",
                "Outcomes", "Barriers", "Plans"
            ])

        new_row = {
            "Grant Code": grant,
            "Report Type": report_type,
            "Period End": report_period,
            "Spent": total_spent,
            "Served": individuals_served,
            "Hours": hours_logged,
            "Outcomes": outcomes,
            "Barriers": barriers,
            "Plans": plan
        }

        log_df = pd.concat([log_df, pd.DataFrame([new_row])], ignore_index=True)
        log_df.to_csv(log_path, index=False)
        st.success(f"✅ Report submitted for {grant} ({report_type}).")
