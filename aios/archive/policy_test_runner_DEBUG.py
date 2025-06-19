import streamlit as st
import csv
import json
import os
import pandas as pd
from query_policy_rag_helper import query_policy_with_synonyms

st.set_page_config(page_title="AI Policy Assistant – Benchmark Test", layout="wide")

st.markdown("## 📊 AI Policy Assistant – Benchmark Test")
st.write("This tool evaluates how well the AI Policy Assistant answers benchmark questions.")

st.markdown("""
- ✅ **Correct** = Matches known policy source  
- ⚠️ **Fallback** = No match, but GPT tries to help  
- ❌ **Miss** = No match, no fallback
""")

# Path to benchmark CSV
csv_path = os.path.abspath("../data/policies/lookup_aids/AI_Policy_Assistant_Test_Questions.csv")

if not os.path.exists(csv_path):
    st.error(f"Test CSV not found at ../data/policies/lookup_aids/AI_Policy_Assistant_Test_Questions.csv")
    st.stop()

results = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for i, row in enumerate(reader):
        question = row[0].strip()
        try:
            result = query_policy_with_synonyms(question)
            st.write(f"**[{i}] {question}**")
            st.json(result)

            if isinstance(result, dict) and result.get("status") == "match":
                label = "✅ Correct"
            elif isinstance(result, dict) and result.get("status") == "fallback":
                label = "⚠️ Fallback"
            else:
                label = "❌ Miss"
        except Exception as e:
            label = "❌ Miss"
            result = {"status": "error", "text": f"⚠️ GPT fallback failed: {e}"}

        results.append({
            "label": label,
            "question": question,
            "answer": result["text"] if isinstance(result, dict) and "text" in result else str(result),
        })

# Display table
df = pd.DataFrame(results)
st.dataframe(df, use_container_width=True)

# Summary
summary = df["label"].value_counts().to_dict()
st.markdown("## 📉 Summary")
st.markdown(f"- ✅ **Correct:** {summary.get('✅ Correct', 0)}")
st.markdown(f"- ⚠️ **Fallback:** {summary.get('⚠️ Fallback', 0)}")
st.markdown(f"- ❌ **Miss:** {summary.get('❌ Miss', 0)}")
st.markdown(f"- **Total:** {len(df)}")

# Save output JSON
output_path = "../data/policies/lookup_aids/ai_helper_test_results.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

st.success(f"Test results saved to {output_path}")
