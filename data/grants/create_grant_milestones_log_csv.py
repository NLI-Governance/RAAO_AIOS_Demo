import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_milestones_log.csv").expanduser()
headers = [
    "Grant Code", "Milestone Title", "Milestone Date",
    "Responsible Party", "Status", "Notes"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ grant_milestones_log.csv created at:", csv_path)
