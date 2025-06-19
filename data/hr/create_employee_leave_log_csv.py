# create_employee_leave_log_csv.py
# Creates a structured CSV to match the leave tracker GUI

import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_leave_log.csv").expanduser()
headers = [
    "Employee Name", "Employee ID", "Leave Type",
    "Start Date", "End Date", "Days Requested",
    "Reason", "Approval Status"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print("✅ employee_leave_log.csv created at:", csv_path)
