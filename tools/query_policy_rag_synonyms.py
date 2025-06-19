# Sample synonym map (expandable booster pack later)
SYNONYM_MAP = {
    "pto": ["paid time off", "vacation", "leave"],
    "harassment": ["bullying", "hostile work environment", "inappropriate behavior"],
    "resignation": ["quit", "notice", "termination by employee"],
    "termination": ["fired", "let go", "dismissed"],
    "disciplinary": ["write-up", "warning", "conduct violation"]
}

def expand_query_with_synonyms(query):
    """
    Replaces known variants in user query with canonical terms for vector matching.
    """
    lowered_query = query.lower()
    for canonical, variants in SYNONYM_MAP.items():
        for variant in variants:
            if variant in lowered_query:
                lowered_query = lowered_query.replace(variant, canonical)
    return lowered_query
