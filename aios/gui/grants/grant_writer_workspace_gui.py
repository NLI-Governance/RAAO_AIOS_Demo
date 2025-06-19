import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

st.set_page_config(page_title="Grant Writer Workspace", layout="centered")

logo_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"
st.image(str(logo_path), width=100)

st.title("📝 Grant Writer Workspace")
st.caption("Use this workspace to draft and save internal grant proposals.")

# Load codes for linking (optional)
code_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv"
codes_df = pd.read_csv(code_path) if code_path.exists() else pd.DataFrame(columns=["Grant Code"])

existing_codes = sorted(codes_df["Grant Code"].dropna().unique().tolist())
grant_option = st.selectbox("Link to Existing Grant Code (optional)", ["None"] + existing_codes)

st.divider()
proposal_title = st.text_input("Proposal Title")
author = st.text_input("Prepared By")
draft_date = st.date_input("Draft Date", value=date.today())

abstract = st.text_area("Abstract ⓘ", help="A brief summary of the proposed project.")
need_statement = st.text_area("Need Statement ⓘ", help="Explain the problem or gap the grant addresses.")
objectives = st.text_area("Objectives ⓘ", help="List 2–3 measurable goals.")

attachments = st.file_uploader("Attach Draft Files (PDF, DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("💾 Save Draft"):
    path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_writer_workspace_log.csv"
    existing = pd.read_csv(path) if path.exists() else pd.DataFrame(columns=[
        "Proposal Title", "Linked Grant Code", "Prepared By", "Date",
        "Abstract", "Need", "Objectives"
    ])

    new_entry = {
        "Proposal Title": proposal_title,
        "Linked Grant Code": grant_option if grant_option != "None" else "",
        "Prepared By": author,
        "Date": draft_date,
        "Abstract": abstract,
        "Need": need_statement,
        "Objectives": objectives
    }

    result = pd.concat([existing, pd.DataFrame([new_entry])], ignore_index=True)
    result.to_csv(path, index=False)
    st.success("✅ Draft saved successfully.")
