import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

headers = [
    "Training Name", "Training Type", "Trainer",
    "File Link", "Expiration Policy", "Notes"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print("✅ training_catalog.csv created at:", csv_path)
