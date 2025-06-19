import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_training_log.csv").expanduser()
headers = [
    "Employee Name", "Employee ID", "Department", "Training Type",
    "Training Name", "Trainer", "Date Completed", "Expiration Date", "Notes"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ employee_training_log.csv created at:", csv_path)
