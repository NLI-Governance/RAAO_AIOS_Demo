import pandas as pd
from pathlib import Path

# Define the path to the CSV file
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_disciplinary_log.csv").expanduser()

# Define the headers for the disciplinary log
headers = [
    "Employee Name", "Employee ID", "Date",
    "Violation Description", "Action Taken",
    "Severity Level", "Follow-up Date", "Notes"
]

# Create an empty DataFrame with the headers
df = pd.DataFrame(columns=headers)

# Save the DataFrame as a CSV file
df.to_csv(csv_path, index=False)
print(f"✅ Disciplinary log CSV created at: {csv_path}")
