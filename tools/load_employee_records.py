import pandas as pd
from pathlib import Path

# File path to employee_records.csv
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_records.csv").expanduser()

# Headers aligned with downstream GUIs
headers = [
    "Full Name", "Email", "Phone", "Start Date", "Employee ID", "Street Address",
    "City", "State", "ZIP Code", "Emergency Contact Name", "Emergency Contact Phone",
    "Department", "Manager", "System Role", "I-9 Verified", "W-4 Received"
]

# Sample entries
sample_data = [
    {
        "Full Name": "Alice Smith",
        "Email": "alice@example.com",
        "Phone": "5551234567",
        "Start Date": "2024-01-10",
        "Employee ID": "EMP0001",
        "Street Address": "123 Main St",
        "City": "Tampa",
        "State": "FL",
        "ZIP Code": "33601",
        "Emergency Contact Name": "Bob Smith",
        "Emergency Contact Phone": "5552223344",
        "Department": "HR",
        "Manager": "Janet Perez",
        "System Role": "Employee",
        "I-9 Verified": "Yes",
        "W-4 Received": "Yes"
    },
    {
        "Full Name": "Bob Jones",
        "Email": "bob@example.com",
        "Phone": "5559876543",
        "Start Date": "2024-03-20",
        "Employee ID": "EMP0002",
        "Street Address": "456 Oak Ave",
        "City": "Miami",
        "State": "FL",
        "ZIP Code": "33101",
        "Emergency Contact Name": "Tom Jones",
        "Emergency Contact Phone": "5553334455",
        "Department": "Operations",
        "Manager": "Maria Lee",
        "System Role": "Employee",
        "I-9 Verified": "Yes",
        "W-4 Received": "Yes"
    }
]

# Create CSV
df = pd.DataFrame(sample_data, columns=headers)
df.to_csv(csv_path, index=False)
print(f"✅ Created: {csv_path}")
