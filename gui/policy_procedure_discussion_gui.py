import streamlit as st
import os

# === Page Setup ===
st.set_page_config(page_title="Policy & Procedure Assistant", layout="wide")
st.markdown("# 📘 Company Policy & Procedure Assistant")
st.markdown("Ask questions about your role, company rules, or workplace policies.")

# === Sidebar for Navigation ===
st.sidebar.title("Navigation")
if st.sidebar.button("⬅️ Return to Employee Menu"):
    st.switch_page("employee_feedback_gui.py")

# === Input Area ===
st.markdown("### 🧠 How can I help you?")
query = st.text_area("Type your policy-related question below or use voice input.", height=150)

# Placeholder for future voice input
st.button("🎤 Start Voice Input (Coming Soon)")

# === Submit Button ===
if st.button("🔍 Ask About Policy"):
    if query.strip() == "":
        st.warning("Please enter a question to proceed.")
    else:
        # Placeholder logic — future upgrade: connect to RAG or doc-based AI
        st.success("✅ This question will be routed to a policy-aware AI system.")
        st.markdown("---")
        st.markdown("**📝 Response (Mock):**")
        st.markdown(f"➡️ *“Here’s what the policy manual says about:* `{query}` *...”*")
        st.info("🔒 Note: All responses will reference official company documents only.")

# === Footer / Help Notice ===
st.markdown("---")
st.caption("⚠️ For legal compliance, always confirm with your supervisor or HR.")
