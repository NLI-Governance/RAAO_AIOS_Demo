
import streamlit as st
import pandas as pd
import traceback
import json
import os
from tools.query_policy_rag_helper import query_policy_with_synonyms

# Path to CSV and output
CSV_PATH = "../data/policies/lookup_aids/AI_Policy_Assistant_Test_Questions.csv"
RESULTS_PATH = "../data/policies/lookup_aids/ai_helper_test_results.json"

st.title("📊 AI Policy Assistant – Benchmark Test")
st.write("This tool evaluates how well the AI Policy Assistant answers benchmark questions.")
st.markdown("""
- ✅ **Correct** = Matches known policy source  
- ⚠️ **Fallback** = No match, but GPT tries to help  
- ❌ **Miss** = No match, no fallback  
""")

# Load benchmark questions
try:
    questions = pd.read_csv(CSV_PATH)
    st.success(f"Loaded {len(questions)} test questions.")
except Exception as e:
    st.error(f"Failed to load test file at {CSV_PATH}")
    st.exception(e)
    st.stop()

# Run evaluation
results = []
for idx, row in questions.iterrows():
    question = row["question"]
    try:
        print(f"🧪 Testing: {question}")
        response = query_policy_with_synonyms(question)
        print("🔄 Response:", response)

        if isinstance(response, dict):
            if response.get("status") == "match":
                label = "✅ Correct"
            elif response.get("status") == "fallback":
                label = "⚠️ Fallback"
            else:
                label = "❌ Miss"
        else:
            label = "❌ Miss"
            response = {"status": "error", "text": str(response)}

    except Exception as e:
        label = "❌ Miss"
        error_text = f"⚠️ GPT fallback failed: {str(e)}"
        print("❌ ERROR:", error_text)
        traceback.print_exc()
        response = {"status": "error", "text": error_text}

    results.append({
        "label": label,
        "question": question,
        "answer": response.get("text") if isinstance(response, dict) else str(response),
    })

# Display results
st.subheader("Running Evaluation...")
st.dataframe(results)

# Summary
correct = sum(1 for r in results if r["label"] == "✅ Correct")
fallback = sum(1 for r in results if r["label"] == "⚠️ Fallback")
miss = sum(1 for r in results if r["label"] == "❌ Miss")
st.subheader("📈 Summary")
st.write(f"- ✅ Correct: {correct}")
st.write(f"- ⚠️ Fallback: {fallback}")
st.write(f"- ❌ Miss: {miss}")
st.write(f"- Total: {len(results)}")

# Save to JSON
try:
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2)
    st.success(f"Test results saved to {RESULTS_PATH}")
except Exception as e:
    st.error("❌ Failed to write test results.")
    st.exception(e)
