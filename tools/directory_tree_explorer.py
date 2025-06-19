import os
from pathlib import Path

ROOT_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25"

def print_tree(path: Path, prefix=""):
    if not path.exists():
        print(f"❌ Path does not exist: {path}")
        return

    contents = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    for index, entry in enumerate(contents):
        connector = "└── " if index == len(contents) - 1 else "├── "
        print(prefix + connector + entry.name)
        if entry.is_dir():
            extension = "    " if index == len(contents) - 1 else "│   "
            print_tree(entry, prefix + extension)

if __name__ == "__main__":
    print(f"\n📂 Directory Tree for: {ROOT_PATH}\n")
    print_tree(ROOT_PATH)
