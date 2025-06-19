import os
import sys
import json
from pathlib import Path
from docx import Document
from openai import OpenAI
import toml

# === Attempt to load API key ===
api_key = None
secrets_path = Path.home() / ".streamlit" / "secrets.toml"
try:
    secrets = toml.load(secrets_path)
    api_key = secrets.get("OPENAI_API_KEY")
except Exception:
    pass

if not api_key:
    sys.path.append(str(Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "gui" / "secrets"))
    try:
        from openai_key import OPENAI_API_KEY
        api_key = OPENAI_API_KEY
    except ImportError:
        print("❌ Failed to load OpenAI API key from both sources.")
        exit(1)

client = OpenAI(api_key=api_key)
print("✅ API key successfully loaded.")

# === Input/output paths ===
source_dir = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "RAAO_sources"
output_path = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "company_policy_index.json"

def extract_text(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text.strip() for para in doc.paragraphs if para.text.strip()])

def generate_qa_pairs(text):
    prompt = (
        "You are an AI assistant. From the following policy document text, generate a list of 3–5 short question-and-answer pairs "
        "that summarize key policy information. Format the response as a JSON array:\n\n"
        f"{text[:3000]}\n\n"
        "Respond only with a JSON array of objects like: [{\"question\": \"...\", \"answer\": \"...\"}, ...]"
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"❌ Error generating from OpenAI: {e}")
        return []

def main():
    all_pairs = []
    for file in sorted(source_dir.glob("*.docx")):
        print(f"📄 Processing: {file.name}")
        try:
            text = extract_text(file)
            qa_pairs = generate_qa_pairs(text)
            all_pairs.extend(qa_pairs)
        except Exception as e:
            print(f"❌ Failed on {file.name}: {e}")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"raao_policies": all_pairs}, f, indent=2)
    print(f"\n✅ GPT-enhanced policy index written to: {output_path}")

if __name__ == "__main__":
    main()
