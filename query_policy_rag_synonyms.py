import json
import os

LOOKUP_DIR = os.path.join(os.path.dirname(__file__), "../data/policies/lookup_aids")

def normalize_query(query: str) -> str:
    with open(os.path.join(LOOKUP_DIR, "keyword_alias_dictionary.json"), "r", encoding="utf-8") as f:
        alias_map = json.load(f)
    for alias, true_term in alias_map.items():
        query = query.replace(alias, true_term)
    return query

def expand_with_synonyms(query: str) -> list:
    with open(os.path.join(LOOKUP_DIR, "synonym_context_expander.json"), "r", encoding="utf-8") as f:
        synonyms = json.load(f)
    words = query.lower().split()
    expanded = set(words)
    for word in words:
        if word in synonyms:
            expanded.update(synonyms[word])
    return list(expanded)
