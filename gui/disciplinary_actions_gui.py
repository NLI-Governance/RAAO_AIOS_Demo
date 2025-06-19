import streamlit as st
import pandas as pd
import sys
import os

st.set_page_config(page_title="Disciplinary Actions", layout="wide")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.query_policy_rag_helper import process_policy_query
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load employee records
@st.cache_data
def load_employee_records():
    path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_records.csv")
    try:
        df = pd.read_csv(path)
        df["Employee ID"] = df["Employee ID"].fillna("Pending ID")
        return df
    except Exception:
        return pd.DataFrame(columns=["Full Name", "Employee ID"])

# Load policy vector index
@st.cache_resource
def load_index_and_docs():
    index_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'policies', 'faiss_index')
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index = FAISS.load_local(index_path, embedding, allow_dangerous_deserialization=True)
    documents = list(index.docstore._dict.values())
    return index, documents

employees = load_employee_records()
index, documents = load_index_and_docs()

st.title("🛑 Disciplinary Action Log")

# Assistant
with st.expander("🧠 Ask a question about disciplinary policy"):
    user_query = st.text_input("Ask a question like 'Can I appeal a write-up?'")
    if user_query:
        response = process_policy_query(user_query, index, documents)
        st.markdown(f"**Answer Method:** `{response['method_used']}`")
        st.markdown(f"**Answer:**\n\n{response['raw_answer']}")
        if isinstance(response["citation_info"], list):
            doc = response["citation_info"][0].get("document", "N/A")
            lines = response["citation_info"][0].get("lines", "N/A")
            st.markdown(f"📄 **Document:** `{doc}`  \n🔖 **Lines:** `{lines}`")

# Form section
st.subheader("📋 Log Disciplinary Incident")

if employees.empty:
    st.warning("⚠️ No employee records found.")
else:
    with st.form("disciplinary_form"):
        name = st.selectbox("Employee Name 🛈", employees["Full Name"])
        emp_row = employees[employees["Full Name"] == name]
        employee_id = emp_row["Employee ID"].values[0] if not emp_row.empty else "Pending ID"

        st.text_input("Employee ID", value=employee_id, disabled=True)
        date = st.date_input("Incident Date")
        reported_by = st.text_input("Reported By 🛈", help="Name of supervisor or team lead reporting this.")
        incident_type = st.selectbox("Type of Infraction 🛈", ["Attendance", "Conduct", "Safety", "Policy Violation"])
        summary = st.text_area("Incident Summary 🛈", help="Brief factual overview of what occurred.")
        resolution = st.text_area("Resolution/Outcome 🛈", help="Describe any coaching, formal warning, or follow-up actions.")
        submit = st.form_submit_button("Log Entry")

    if submit:
        st.success(f"Disciplinary action for {name} recorded.")

# Example table
st.subheader("🗂️ Incident Log (example)")
sample = {
    "Employee": ["Alice Smith", "Bob Jones"],
    "Date": ["2024-04-15", "2024-05-02"],
    "Type": ["Conduct", "Attendance"],
    "Reported By": ["Supervisor A", "Supervisor B"]
}
df = pd.DataFrame(sample)
st.dataframe(df)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Disciplinary Log", data=csv, file_name="disciplinary_log.csv")
