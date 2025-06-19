import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/payroll_summary.csv").expanduser()

headers = [
    "Employee Name", "Employee ID", "Period Start", "Period End",
    "Total Hours", "Base Pay", "Overtime", "Funding Source(s)", "Total Pay"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ payroll_summary.csv created at:", csv_path)
