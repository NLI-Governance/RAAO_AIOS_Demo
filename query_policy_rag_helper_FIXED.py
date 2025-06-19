from aios_secrets.openai_key import openai_api_key
from tools.query_policy_rag_synonyms import normalize_query, expand_with_synonyms
from tools.query_policy_rag_core import get_policy_answer

def query_policy_with_synonyms(user_query: str):
    normalized = normalize_query(user_query)
    expanded = expand_with_synonyms(normalized)
    return get_policy_answer(expanded)
