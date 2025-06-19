import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_benefits_log.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

headers = [
    "Name", "Employee ID", "Department",
    "Medical", "Dental", "Vision",
    "Retirement", "Life Insurance",
    "Enrollment Date", "Notes"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print("✅ employee_benefits_log.csv created at:", csv_path)
