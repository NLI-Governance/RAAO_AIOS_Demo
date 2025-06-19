import json
from pathlib import Path

POLICY_INDEX_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "company_policy_index.json"

with open(POLICY_INDEX_PATH, "r", encoding="utf-8") as f:
    policies = json.load(f)

print("\n✅ Listing all indexed policy questions:\n")
for category, entries in policies.items():
    print(f"\n📂 Category: {category}")
    for item in entries:
        print(f"  • {item['question']}")
