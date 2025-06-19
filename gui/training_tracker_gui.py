import streamlit as st
import pandas as pd
import sys
import os

st.set_page_config(page_title="Training Tracker", layout="wide")
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

# Load FAISS index
@st.cache_resource
def load_index_and_docs():
    index_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'policies', 'faiss_index')
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index = FAISS.load_local(index_path, embedding, allow_dangerous_deserialization=True)
    documents = list(index.docstore._dict.values())
    return index, documents

employees = load_employee_records()
index, documents = load_index_and_docs()

st.title("📘 Training Tracker")

# Assistant section
with st.expander("🧠 Ask a question about training policy"):
    user_query = st.text_input("Type your question here:")
    if user_query:
        response = process_policy_query(user_query, index, documents)
        st.markdown(f"**Answer Method:** `{response['method_used']}`")
        st.markdown(f"**Answer:**\n\n{response['raw_answer']}")
        if isinstance(response["citation_info"], list):
            doc = response["citation_info"][0].get("document", "N/A")
            lines = response["citation_info"][0].get("lines", "N/A")
            st.markdown(f"📄 **Document:** `{doc}`  \n🔖 **Lines:** `{lines}`")

# Training form
st.subheader("📋 Log New Training Record")

if employees.empty:
    st.warning("⚠️ No employee records found. Please verify `employee_records.csv`.")
else:
    with st.form("training_form"):
        name = st.selectbox("Employee Name", employees["Full Name"])
        matching_row = employees[employees["Full Name"] == name]

        if not matching_row.empty:
            employee_id = matching_row["Employee ID"].values[0]
        else:
            employee_id = "Pending ID"

        st.text_input("Employee ID", value=employee_id, disabled=True)

        training_title = st.selectbox("Training Title", ["OSHA Safety", "Onboarding", "Harassment Prevention", "Job-Specific"])
        date_completed = st.date_input("Date Completed")
        cert_expiration = st.date_input("Certification Expiration")
        submit = st.form_submit_button("Add Record")

    if submit:
        st.success(f"Training record for {name} added.")

# Example data log
st.subheader("🗂️ Existing Records (example)")
data = {
    "Employee": ["Alice Smith", "Bob Jones"],
    "Training": ["OSHA Safety", "Harassment Prevention"],
    "Completed": ["2024-03-01", "2024-06-01"],
    "Expires": ["2025-03-01", "2025-06-01"]
}
df = pd.DataFrame(data)
st.dataframe(df)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Training Log", data=csv, file_name="training_log.csv")
