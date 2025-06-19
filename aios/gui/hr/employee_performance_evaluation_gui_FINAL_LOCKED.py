import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

st.set_page_config(page_title="Employee Performance Evaluation", layout="centered")

st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)
st.title("📝 Employee Performance Evaluation")
st.markdown("Evaluate employee performance, set goals, and provide feedback.")

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_performance_log.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

with st.form("performance_form"):
    name = st.text_input("Employee Full Name", help="Enter the full legal name of the employee.")
    emp_id = st.text_input("Employee ID", help="Unique identifier assigned to the employee.")
    evaluator = st.text_input("Evaluator Name", help="Person conducting this evaluation.")
    department = st.text_input("Department", help="The employee’s department.")

    st.markdown("---")
    st.subheader("Evaluation Metrics")

    punctuality = st.slider("Punctuality (1 = Poor, 5 = Excellent)", 1, 5, help="Rate how consistently the employee arrives on time.")
    teamwork = st.slider("Teamwork (1 = Poor, 5 = Excellent)", 1, 5, help="Rate how well the employee collaborates with others.")
    productivity = st.slider("Productivity (1 = Poor, 5 = Excellent)", 1, 5, help="Rate the overall output of the employee.")
    initiative = st.slider("Initiative (1 = Poor, 5 = Excellent)", 1, 5, help="Rate the employee’s willingness to take proactive steps.")

    comments = st.text_area("Evaluator Comments", help="Include any additional feedback or context for the evaluation.")
    goals = st.text_area("Future Goals", help="Document specific performance goals for the next review period.")

    submitted = st.form_submit_button("Submit Evaluation")

if submitted:
    new_record = pd.DataFrame([{
        "Date": date.today(),
        "Employee Name": name,
        "Employee ID": emp_id,
        "Evaluator": evaluator,
        "Department": department,
        "Punctuality": punctuality,
        "Teamwork": teamwork,
        "Productivity": productivity,
        "Initiative": initiative,
        "Comments": comments,
        "Goals": goals
    }])

    if csv_path.exists():
        existing = pd.read_csv(csv_path)
        combined = pd.concat([existing, new_record], ignore_index=True)
    else:
        combined = new_record

    combined.to_csv(csv_path, index=False)
    st.success("✅ Performance evaluation submitted successfully.")
