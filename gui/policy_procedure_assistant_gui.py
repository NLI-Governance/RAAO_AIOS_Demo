import streamlit as st
import json
import os

# Path to live policy index
policy_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/policies/company_policy_index.json")

def load_policies():
    with open(policy_path, "r") as f:
        return json.load(f)

def search_policy(question, policies):
    # Simple match by keyword in title or body
    results = []
    q_lower = question.lower()
    for category, entries in policies.items():
        for entry in entries:
            if q_lower in entry["title"].lower() or q_lower in entry["text"].lower():
                results.append((entry["title"], entry["text"]))
    return results

# --- UI ---
st.set_page_config(page_title="Policy & Procedure Assistant", layout="centered")
st.title("📘 Company Policy & Procedure Assistant")
st.write("Ask questions about your role, company rules, or workplace policies.")

st.subheader("🧠 How can I help you?")
user_input = st.text_area("Type your policy-related question below:", height=120)
submit = st.button("🔍 Ask About Policy")

if submit and user_input:
    try:
        policies = load_policies()
        matches = search_policy(user_input, policies)

        if matches:
            for title, text in matches:
                st.success(f"📘 **{title}**\n\n{text}")
        else:
            st.warning("No exact match found. Please rephrase or try a different term.")

    except Exception as e:
        st.error(f"Failed to load policies: {e}")

st.markdown("""
---
⚠️ *For legal compliance, always confirm policy interpretations with your supervisor or HR.*
""")
