import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_funding_log.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

headers = ["Grant Name", "Grant Code", "Amount", "Date", "Description"]
df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print(f"✅ grant_funding_log.csv created at: {csv_path}")
