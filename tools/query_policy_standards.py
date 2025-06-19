import difflib
from pathlib import Path

STANDARD_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "policy_standards_reference.md"

def load_standards_text():
    if not STANDARD_PATH.exists():
        raise FileNotFoundError(f"Standards reference not found: {STANDARD_PATH}")
    with open(STANDARD_PATH, "r", encoding="utf-8") as f:
        return f.read()

def extract_matches(query, content, threshold=0.4):
    lines = content.splitlines()
    # Fuzzy match first
    fuzzy = difflib.get_close_matches(query.lower(), [line.lower() for line in lines], n=10, cutoff=threshold)
    # Substring fallback
    fallback = [line for line in lines if query.lower() in line.lower()]
    combined = list(set(fuzzy + fallback))
    return [line for line in lines if line.lower() in combined]

if __name__ == "__main__":
    print("✅ Standards reference loaded.\n")
    content = load_standards_text()

    while True:
        query = input("🔎 Enter keyword to search (or type 'exit' to quit): ").strip()
        if query.lower() in ["exit", "quit"]:
            break

        results = extract_matches(query, content)
        if results:
            print("\n📌 Matches found:\n")
            for line in results:
                print("•", line.strip())
        else:
            print("⚠️ No matches found. Try rephrasing.\n")
