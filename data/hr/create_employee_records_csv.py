import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_records.csv").expanduser()
headers = [
    "Full Name", "Email", "Phone", "Start Date", "Employee ID", "Street Address",
    "City", "State", "ZIP Code", "Emergency Contact Name", "Emergency Contact Phone",
    "Department", "Manager", "System Role", "I-9 Verified", "W-4 Received"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ employee_records.csv created at:", csv_path)
