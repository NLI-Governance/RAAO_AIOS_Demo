import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/volunteer_roles.csv").expanduser()
headers = ["Role Name", "Description", "Is Active"]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ volunteer_roles.csv created at:", csv_path)
