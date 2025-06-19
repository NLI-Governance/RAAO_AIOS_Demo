import json
import os
from pathlib import Path
from difflib import get_close_matches

# Load policy index file
POLICY_INDEX_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "company_policy_index.json"

def load_policies():
    if not POLICY_INDEX_PATH.exists():
        raise FileNotFoundError(f"Policy file not found at {POLICY_INDEX_PATH}")
    with open(POLICY_INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_best_policy_match(query, policies):
    topics = []
    mapping = {}
    for category in policies:
        for entry in policies[category]:
            phrase = entry["question"].strip()
            topics.append(phrase)
            mapping[phrase] = entry["answer"]

    # Try looser cutoff for better reach
    close = get_close_matches(query.strip(), topics, n=1, cutoff=0.4)
    if close:
        match = close[0]
        return match, mapping[match]
    else:
        return None, None

if __name__ == "__main__":
    try:
        policies = load_policies()
        print("\n✅ Loaded policy categories:")
        for cat in policies:
            print(f" - {cat}")

        user_question = input("\n🔎 Enter your policy question: ")
        match, answer = find_best_policy_match(user_question, policies)

        if match:
            print(f"\n📄 Closest policy match:\n - {match}\n\n✅ Policy guidance:\n{answer}")
        else:
            print("\n⚠️ No matching policy topic found.")
            print("💡 Try rephrasing with simpler keywords or breaking your question into shorter phrases.")

    except Exception as e:
        print(f"❌ Error: {e}")
