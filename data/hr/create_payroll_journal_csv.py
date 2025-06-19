from pathlib import Path
import pandas as pd

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/payroll_journal.csv").expanduser()

headers = [
    "Employee Name", "Employee ID", "Pay Period Start", "Pay Period End",
    "Total Hours", "Base Pay", "Overtime Pay", "Funding Source Breakdown",
    "Total Gross Pay", "Deductions", "Net Pay"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print("✅ payroll_journal.csv created at:", csv_path)
