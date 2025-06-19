import pandas as pd
from pathlib import Path

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/job_postings.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

headers = [
    "Position Title", "Department", "Job Type", "Location", "Start Date",
    "Salary Range", "Benefits", "Job Description", "Qualifications", "Application Deadline"
]

df = pd.DataFrame(columns=headers)
df.to_csv(csv_path, index=False)

print("✅ job_postings.csv created at:", csv_path)
