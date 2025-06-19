import json
from pathlib import Path
from query_policy_rag_synonyms import normalize_query, expand_with_synonyms

# Load supporting files from lookup directory
LOOKUP_DIR = Path(__file__).resolve().parent.parent / "data/policies/lookup_aids"

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

fallback_topics = load_json(LOOKUP_DIR / "rag_fallback_topics.json")
alias_map = load_json(LOOKUP_DIR / "keyword_alias_dictionary.json")
synonym_map = load_json(LOOKUP_DIR / "synonym_context_expander.json")

def query_policy_with_synonyms(query):
    """
    Main RAG search logic for structured fallback assistance.
    - Normalizes user input (e.g., HIPPA → HIPAA)
    - Expands with synonyms (e.g., dress code → uniform, appearance)
    - Searches fallback index for matches
    """
    # Normalize first using alias map
    normalized_query = normalize_query(query, alias_map)

    # Expand with synonym clusters
    expanded_queries = expand_with_synonyms(normalized_query, synonym_map)

    # Search fallback topics
    for phrase in expanded_queries:
        for topic, patterns in fallback_topics.items():
            if any(phrase.lower() in match.lower() for match in patterns):
                return {
                    "match_type": "structured",
                    "matched_topic": topic,
                    "phrases_tested": expanded_queries,
                    "raw_query": query
                }

    # No match found — trigger fallback
    return {
        "match_type": "fallback",
        "matched_topic": None,
        "phrases_tested": expanded_queries,
        "raw_query": query
    }
