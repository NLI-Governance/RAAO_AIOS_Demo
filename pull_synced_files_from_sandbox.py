import os
import shutil
from pathlib import Path

# Sandbox-to-Dropbox path mapping (manual mirror)
sandbox_root = Path("/mnt/data/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/")
local_root = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25"

# File list to sync (you can add to this list)
files_to_sync = [
    "gui/policy_test_runner.py",
    "gui/policy_procedure_rag_gui.py",
    "gui/policy_query_tester_gui.py",
    "gui/query_log_export_tool.py",
    "gui/language_toggle_component.py"
]

print("📥 Syncing files from sandbox to local Dropbox folder...\n")

for relative_path in files_to_sync:
    src = sandbox_root / relative_path
    dst = local_root / relative_path

    dst.parent.mkdir(parents=True, exist_ok=True)

    try:
        shutil.copy2(src, dst)
        print(f"✅ {relative_path} copied.")
    except Exception as e:
        print(f"❌ Failed to copy {relative_path}: {e}")

print("\n✅ Sync complete. You can now run synced files directly.")
