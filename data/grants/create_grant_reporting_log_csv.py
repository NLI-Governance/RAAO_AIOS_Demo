import pandas as pd
from pathlib import Path

# Define CSV path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_reporting_log.csv").expanduser()

# Define headers
headers = [
    "Grant Name", "Report Type", "Reporting Period Start", "Reporting Period End",
    "Total Spent", "Funding Balance", "Narrative Summary", "Submitted By", "Submission Date"
]

# Create and save DataFrame
df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print(f"✅ grant_reporting_log.csv created at: {csv_path}")
