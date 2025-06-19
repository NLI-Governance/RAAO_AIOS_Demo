import streamlit as st
import pandas as pd
import json

log_file = "../data/policies/lookup_aids/policy_query_log.json"
st.title("📦 Export Policy Query Log")

try:
    with open(log_file, "r") as f:
        logs = json.load(f)
    df = pd.DataFrame(logs)
except:
    df = pd.DataFrame()

if df.empty:
    st.warning("No query logs available.")
else:
    filter_option = st.selectbox("Filter", ["All", "Unmatched Only (GPT)", "Fallback Only"])

    if filter_option == "Unmatched Only (GPT)":
        filtered = df[df["method"] == "GPT"]
    elif filter_option == "Fallback Only":
        filtered = df[df["method"] == "Fallback"]
    else:
        filtered = df

    st.dataframe(filtered)
    st.download_button("Download CSV", filtered.to_csv(index=False), "policy_query_log_export.csv")
