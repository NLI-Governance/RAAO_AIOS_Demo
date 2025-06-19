import os
import csv
import re
from pathlib import Path

# === CONFIGURATION ===
GUI_DIR = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "gui"
DATA_DIR = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data"
TARGET_EXT = ".py"
CSV_EXT = ".csv"

def extract_csv_paths_from_gui(gui_path):
    with open(gui_path, "r") as f:
        lines = f.readlines()

    csv_files = []
    for line in lines:
        match = re.search(r'(?:pd\.read_csv|to_csv)\([\'"](.+?\.csv)[\'"]', line)
        if match:
            csv_files.append(match.group(1))
    return csv_files

def get_all_gui_files(root_dir):
    return [p for p in root_dir.rglob(f'*{TARGET_EXT}') if 'test_' not in p.name and not p.name.startswith("__")]

def get_csv_headers(csv_path):
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            return reader.fieldnames
    except Exception as e:
        return [f"(Error reading CSV: {e})"]

def audit_gui_csv_links():
    report = []
    gui_files = get_all_gui_files(GUI_DIR)

    for gui_file in gui_files:
        csv_refs = extract_csv_paths_from_gui(gui_file)
        report.append(f"\n🔍 GUI: {gui_file.relative_to(GUI_DIR)}")
        if not csv_refs:
            report.append("  ⚠️  No CSV references found.")
            continue

        for csv_ref in csv_refs:
            potential_paths = list(DATA_DIR.rglob(csv_ref))
            if not potential_paths:
                report.append(f"  ❌ CSV not found: {csv_ref}")
            else:
                for path in potential_paths:
                    headers = get_csv_headers(path)
                    report.append(f"  ✅ Found: {path.relative_to(DATA_DIR)}")
                    report.append(f"     Columns: {headers}")

    return "\n".join(report)

if __name__ == "__main__":
    print("📋 AIOS System Integrity Audit")
    print("=" * 40)
    result = audit_gui_csv_links()
    print(result)
