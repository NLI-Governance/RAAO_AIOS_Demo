import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv").expanduser()
headers = [
    "Grant Code", "Funding Source", "Start Date", "End Date",
    "Amount", "Notes"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ grant_codes.csv created at:", csv_path)
