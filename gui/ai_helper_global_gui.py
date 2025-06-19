# ai_helper_global_gui.py
# GPT assistant updated for OpenAI SDK v1.0+

import streamlit as st
import os
import sys
import openai

# Secure API key import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "secrets")))
from openai_key import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="AI Assistant", layout="centered")
st.image("logo.png", width=120)
st.title("🧠 AI Assistant — Internal Helpdesk")

role = st.selectbox("Select Your Role", ["Employee", "HR", "Supervisor", "Admin"])
st.info(f"Role permissions set to: **{role}**")

with st.form("ai_form"):
    query = st.text_area(
        "What would you like help with? 🛈",
        help="""Use this assistant to:

• Rewrite HR letters, memos, or reports  
• Clarify form requirements  
• Understand grant, training, or onboarding policies  
• Rephrase sensitive info with professionalism

⚠️ Avoid using for legal, disciplinary, or medical judgments without HR leadership approval.
"""
    )
    submitted = st.form_submit_button("Ask the Assistant")

if submitted and query:
    with st.spinner("Thinking..."):
        try:
            client = openai.OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are a helpful, compliant assistant supporting the role: {role}."},
                    {"role": "user", "content": query}
                ],
                temperature=0.6,
                max_tokens=600
            )
            answer = response.choices[0].message.content
            st.success("AI Response:")
            st.markdown(answer)

        except Exception as e:
            st.error("⚠️ Assistant error:")
            st.exception(e)

st.markdown("---")
st.markdown("© 2025 Rising Against All Odds | GPT v1 API Ready")
