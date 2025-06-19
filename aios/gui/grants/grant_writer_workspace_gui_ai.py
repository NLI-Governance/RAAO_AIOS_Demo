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

# OpenAI API key input
api_key = st.text_input("Enter OpenAI API Key ⓘ", type="password", help="ⓘ Required to generate AI suggestions. Your key is not stored.")
if api_key:
    openai.api_key = api_key

# Grant linking
code_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv"
codes_df = pd.read_csv(code_path) if code_path.exists() else pd.DataFrame(columns=["Grant Code"])
existing_codes = sorted(codes_df["Grant Code"].dropna().unique().tolist())
grant_option = st.selectbox("Link to Existing Grant Code ⓘ", ["None"] + existing_codes, help="ⓘ Optional: Connect this draft to a previously entered grant code for consistency.")

# Input fields
proposal_title = st.text_input("Proposal Title ⓘ", help="ⓘ Title of the proposed grant. This helps the AI generate contextually relevant drafts.")
author = st.text_input("Prepared By ⓘ", help="ⓘ Your name or team. This is logged for tracking draft ownership.")
draft_date = st.date_input("Draft Date ⓘ", value=date.today(), help="ⓘ Date this draft was created. Useful for version history.")

# Narrative areas
abstract = st.text_area("Abstract ⓘ", height=150, help="ⓘ High-level summary of your proposal. The AI will offer suggestions using this field.")
need_statement = st.text_area("Need Statement ⓘ", height=150, help="ⓘ Describe the problem or gap. This helps the AI understand urgency and rationale.")
objectives = st.text_area("Objectives ⓘ", height=150, help="ⓘ What goals do you intend to accomplish? The AI can generate SMART objectives here.")

# AI Buttons and generation
if st.button("💡 Suggest Abstract with AI"):
    if not api_key:
        st.warning("Please enter your OpenAI API key to use this feature.")
    elif proposal_title:
        try:
            prompt = f"Draft a professional abstract for a grant proposal titled '{proposal_title}'."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.generated_abstract = response.choices[0].message.content
            st.info("AI Suggestion Complete. You can copy-paste it into the abstract field above.")
            st.code(st.session_state.generated_abstract)
        except Exception as e:
            st.error(f"Error from OpenAI: {e}")
    else:
        st.warning("Please enter a Proposal Title first.")

if st.button("📌 Suggest Need Statement"):
    if not api_key:
        st.warning("Please enter your OpenAI API key to use this feature.")
    else:
        try:
            prompt = "Write a need statement for a nonprofit addressing underserved populations in community health."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.generated_need = response.choices[0].message.content
            st.info("AI Suggestion Complete. Copy into the field above if useful.")
            st.code(st.session_state.generated_need)
        except Exception as e:
            st.error(f"Error from OpenAI: {e}")

if st.button("🎯 Generate Objectives"):
    if not api_key:
        st.warning("Please enter your OpenAI API key to use this feature.")
    else:
        try:
            prompt = "List three SMART objectives for a harm reduction outreach program."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.generated_objectives = response.choices[0].message.content
            st.info("AI Suggestion Complete. Paste the generated objectives above if helpful.")
            st.code(st.session_state.generated_objectives)
        except Exception as e:
            st.error(f"Error from OpenAI: {e}")

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
