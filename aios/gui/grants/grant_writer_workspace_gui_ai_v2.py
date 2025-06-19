import streamlit as st
from pathlib import Path
import openai

st.set_page_config(page_title="AI Grant Writer Workspace", layout="centered")

# Logo
logo_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"
st.image(str(logo_path), width=100)

st.title("🧠 AI Grant Writer Workspace")
st.caption("Use this form to draft proposal components and generate AI-assisted language.")

with st.form("grant_writer_form"):
    project_title = st.text_input("Project Title", help="ⓘ Title of the proposed grant project.")
    agency_name = st.text_input("Funding Agency", help="ⓘ Name of the organization providing the grant.")
    target_audience = st.text_area("Target Audience", help="ⓘ Who is being served? e.g., low-income families, rural veterans, students.")
    budget_scope = st.text_area("Budget Scope", help="ⓘ What will funds cover? e.g., salaries, supplies, outreach.")
    objectives = st.text_area("Key Objectives", help="ⓘ What specific outcomes should this grant achieve?")
    deliverables = st.text_area("Deliverables", help="ⓘ Tangible outputs. e.g., # of people trained, materials created.")
    timeline = st.text_input("Proposed Timeline", help="ⓘ Summary of the grant period or milestones. e.g., Jan–Dec 2026")

    submit = st.form_submit_button("Generate AI Suggestions")

if submit:
    st.warning("⚠️ AI content generation is placeholder-only. Connect secure API key to activate suggestion generation.")
