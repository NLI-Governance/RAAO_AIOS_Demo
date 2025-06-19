import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date
import openai
import sys

# Point to local secrets folder
secrets_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/secrets"
sys.path.append(str(secrets_path))

# Secure API key load
from openai_key import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="AI Grant Writer Workspace", layout="centered")

# Logo
logo_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"
st.image(str(logo_path), width=100)

st.title("🤖 AI Grant Writer Workspace")
st.caption("Draft grant proposals with AI-assisted narrative support.")

# Form layout
with st.form("grant_form"):
    proposal_title = st.text_input("Proposal Title", help="ⓘ What is the title of the grant proposal?")
    prepared_by = st.text_input("Prepared By", help="ⓘ Name of the preparer or organization.")
    draft_date = st.date_input("Draft Date", value=date.today(), help="ⓘ Date this draft was created.")
    
    abstract = st.text_area("Abstract", height=120, help="ⓘ High-level summary of your project.")
    need = st.text_area("Statement of Need", height=120, help="ⓘ Explain the issue or problem being addressed.")
    objectives = st.text_area("Objectives", height=120, help="ⓘ What specific goals will this grant accomplish?")
    deliverables = st.text_area("Deliverables", height=120, help="ⓘ Tangible results of the grant (e.g., reports, trainings).")
    
    submit = st.form_submit_button("Generate Suggestions")

# AI suggestion placeholder
if submit:
    st.info("🧠 AI response will appear below. Suggestions are based on your inputs.")
    try:
        prompt = f"Write a grant abstract for a project titled '{proposal_title}', targeting: {need}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        suggestion = response.choices[0].message.content
        st.success("✅ AI Abstract Suggestion:")
        st.code(suggestion)
    except Exception as e:
        st.error(f"⚠️ Error generating suggestion: {e}")
