from tools.query_policy_rag_synonyms import normalize_query, expand_with_synonyms

def query_policy_with_synonyms(raw_query: str):
    query = normalize_query(raw_query)
    expanded_terms = expand_with_synonyms(query)
    return {
        "normalized": query,
        "expanded_terms": expanded_terms,
        "results": f"(simulated) Searching index for: {expanded_terms}"
    }
