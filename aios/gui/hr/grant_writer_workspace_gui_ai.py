# PART 1: Create file and directory
# mkdir -p ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/grants && nano ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/grants/grant_writer_workspace_gui_ai.py

# PART 2: Full AI-enhanced Script
import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date
import openai

st.set_page_config(page_title="AI Grant Writer Workspace", layout="centered")

# Logo
logo_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"
st.image(str(logo_path), width=100)

st.title("🤖 AI Grant Writer Workspace")
st.caption("Draft grant proposals with AI-assisted abstract, need, and objective generation.")

# Grant linking
code_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv"
codes_df = pd.read_csv(code_path) if code_path.exists() else pd.DataFrame(columns=["Grant Code"])
existing_codes = sorted(codes_df["Grant Code"].dropna().unique().tolist())
grant_option = st.selectbox("Link to Existing Grant Code (optional)", ["None"] + existing_codes)

# Input fields
proposal_title = st.text_input("Proposal Title")
author = st.text_input("Prepared By")
draft_date = st.date_input("Draft Date", value=date.today())

# Narrative areas
abstract = st.text_area("Abstract", height=150)
need_statement = st.text_area("Need Statement", height=150)
objectives = st.text_area("Objectives", height=150)

# AI Buttons and generation
if st.button("💡 Suggest Abstract with AI"):
    if proposal_title:
        prompt = f"Draft a professional abstract for a grant proposal titled '{proposal_title}'."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        st.session_state.generated_abstract = response.choices[0].message.content
        st.info("AI Suggestion Complete. You can copy-paste it into the abstract field above.")
        st.code(st.session_state.generated_abstract)
    else:
        st.warning("Please enter a Proposal Title first.")

if st.button("📌 Suggest Need Statement"):
    prompt = "Write a need statement for a nonprofit addressing underserved populations in community health."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    st.session_state.generated_need = response.choices[0].message.content
    st.info("AI Suggestion Complete. Copy into the field above if useful.")
    st.code(st.session_state.generated_need)

if st.button("🎯 Generate Objectives"):
    prompt = "List three SMART objectives for a harm reduction outreach program."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    st.session_state.generated_objectives = response.choices[0].message.content
    st.info("AI Suggestion Complete. Paste the generated objectives above if helpful.")
    st.code(st.session_state.generated_objectives)

# Save entry
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

# PART 3: Streamlit Command
# streamlit run ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/grants/grant_writer_workspace_gui_ai.py
