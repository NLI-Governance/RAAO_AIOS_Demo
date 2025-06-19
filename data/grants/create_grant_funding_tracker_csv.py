import pandas as pd
from pathlib import Path

# Define the CSV file path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_funding_tracker.csv").expanduser()

# Define the CSV headers
headers = [
    "Grant Name", "Grant Code", "Amount Spent", "Category", "Description",
    "Date", "Entered By"
]

# Create the empty DataFrame and save to CSV
df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)
print(f"✅ grant_funding_tracker.csv created at: {csv_path}")
