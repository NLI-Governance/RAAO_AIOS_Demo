import os, json
from pathlib import Path

SOURCE_DIR = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "RAAO_sources"
OUTPUT_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "company_policy_index.json"

def clean_text(text):
    return text.replace("\n", " ").strip()

def extract_policy_blocks():
    policy_index = {}
    for file in SOURCE_DIR.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        category = file.stem.lower().replace(" ", "_")
        policy_index[category] = {
            "title": file.stem,
            "rules": [clean_text(line) for line in lines]
        }
    return policy_index

if __name__ == "__main__":
    index = extract_policy_blocks()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(f"✅ Policy index written to {OUTPUT_PATH}")
