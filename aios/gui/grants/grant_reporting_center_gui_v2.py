import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

logo_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"
st.image(str(logo_path), width=120)
st.title("📄 Grant Reporting Center")
st.caption("Compile and submit grant compliance reports with financial, outcome, and narrative data.")

# Load grant codes
codes_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv"
codes_df = pd.read_csv(codes_path)
grant_names = sorted(codes_df["Grant Code"].dropna().unique().tolist())

with st.form("report_form"):
    st.subheader("Grant Details")

    grant = st.selectbox(
        "Grant Code ⓘ", grant_names,
        help="Select the funding source you are reporting on. Grant codes are defined in the Grant Code Manager."
    )
    report_type = st.selectbox(
        "Report Type ⓘ", ["Quarterly", "Annual", "Custom"],
        help="Choose the type of report being submitted. Custom is for non-standard reporting cycles."
    )
    report_period = st.date_input(
        "Period Ending ⓘ", value=date.today(),
        help="Date this reporting period ends. Typically the last day of the quarter or year."
    )

    st.divider()
    st.subheader("Summary Metrics")

    total_spent = st.number_input(
        "Total Funds Spent ($) ⓘ", min_value=0.0, step=100.0,
        help="Enter the total amount spent from the grant during the reporting period."
    )
    individuals_served = st.number_input(
        "Individuals Served ⓘ", min_value=0, step=1,
        help="Count of unique individuals reached with grant-funded services."
    )
    hours_logged = st.number_input(
        "Total Staff Hours ⓘ", min_value=0.0, step=1.0,
        help="Total number of staff hours funded by this grant during the reporting period."
    )

    st.divider()
    st.subheader("Narrative Components")

    outcomes = st.text_area(
        "Outcomes Achieved ⓘ",
        help="Briefly describe accomplishments and impact of the grant during the period."
    )
    barriers = st.text_area(
        "Barriers Encountered ⓘ",
        help="Describe any delays, staffing gaps, or external challenges impacting outcomes."
    )
    plan = st.text_area(
        "Plans for Next Period ⓘ",
        help="Summarize intended activities, goals, or improvements for the next reporting period."
    )

    st.file_uploader(
        "Attach Additional Report File (PDF, DOCX, JPG) ⓘ",
        type=["pdf", "docx", "jpg"],
        help="Optional upload of full narrative or visual documentation."
    )

    submitted = st.form_submit_button("Submit Grant Report")

    if submitted:
        log_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_reports.csv"
        log_exists = log_path.exists()

        if log_exists:
            log_df = pd.read_csv(log_path)
        else:
            log_df = pd.DataFrame(columns=[
                "Grant Code", "Report Type", "Period End",
                "Total Spent", "Individuals Served", "Hours Logged",
                "Outcomes", "Barriers", "Next Plans"
            ])

        new_row = {
            "Grant Code": grant,
            "Report Type": report_type,
            "Period End": report_period,
            "Total Spent": total_spent,
            "Individuals Served": individuals_served,
            "Hours Logged": hours_logged,
            "Outcomes": outcomes,
            "Barriers": barriers,
            "Next Plans": plan
        }

        log_df = pd.concat([log_df, pd.DataFrame([new_row])], ignore_index=True)
        log_df.to_csv(log_path, index=False)
        st.success(f"✅ Grant report submitted for {grant}.")
