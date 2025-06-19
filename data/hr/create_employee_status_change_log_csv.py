import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_status_change_log.csv").expanduser()

headers = [
    "Employee Name",
    "Employee ID",
    "Previous Role",
    "New Role",
    "Previous Department",
    "New Department",
    "Effective Date",
    "Reason for Change",
    "Approved By"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print(f"✅ employee_status_change_log.csv created at: {csv_path}")
