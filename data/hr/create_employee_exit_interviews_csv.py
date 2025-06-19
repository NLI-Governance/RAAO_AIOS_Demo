import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_exit_interviews.csv").expanduser()
headers = [
    "Employee Name", "Employee ID", "Department",
    "Last Day", "Reason for Leaving", "Exit Comments"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print(f"✅ employee_exit_interviews.csv created at: {csv_path}")
