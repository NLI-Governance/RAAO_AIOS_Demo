import streamlit as st

st.set_page_config(page_title="RAAO Navigation Menu", layout="wide")
st.title("📍 Central Navigation Menu")

st.write("Welcome to the AIOS system. Choose a module below:")
st.page_link("grants/grant_writer_workspace_gui.py", label="Grant Writer Workspace", icon="📝")
st.page_link("grants/grant_funding_tracker_gui.py", label="Grant Tracker", icon="📊")
st.page_link("hr/employee_application_gui.py", label="Employee Applications", icon="📋")
st.page_link("training/training_tracker_gui.py", label="Training Tracker", icon="🎓")
st.page_link("payroll/payroll_timecode_entry_gui.py", label="Payroll Entry", icon="🕓")