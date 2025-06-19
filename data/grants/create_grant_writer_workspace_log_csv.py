import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_writer_workspace_log.csv").expanduser()

headers = [
    "Proposal Title", "Linked Grant Code", "Prepared By", "Date",
    "Abstract", "Need", "Objectives"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print(f"✅ grant_writer_workspace_log.csv created at: {csv_path}")
