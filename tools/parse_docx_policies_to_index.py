import os
import json
from pathlib import Path
from docx import Document

DOCX_DIR = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "RAAO_sources"
OUTPUT_PATH = DOCX_DIR.parent / "company_policy_index.json"

def extract_qa_pairs(docx_path):
    doc = Document(docx_path)
    qa_list = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text.lower().startswith("q:") or text.lower().startswith("question:"):
            question = text.split(":", 1)[1].strip()
            continue
        elif text.lower().startswith("a:") or text.lower().startswith("answer:"):
            answer = text.split(":", 1)[1].strip()
            if question:
                qa_list.append({"question": question, "answer": answer})
                question = None

    return qa_list

def build_index():
    index = {"raao_policies": []}
    for file in DOCX_DIR.glob("*.docx"):
        print(f"📄 Processing: {file.name}")
        qa = extract_qa_pairs(file)
        index["raao_policies"].extend(qa)
    return index

if __name__ == "__main__":
    index = build_index()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(f"\n✅ RAAO policy index written to: {OUTPUT_PATH}")
