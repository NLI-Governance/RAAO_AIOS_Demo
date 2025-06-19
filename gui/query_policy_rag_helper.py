from tools.query_policy_rag_core import get_top_rag_results
from tools.query_policy_rag_synonyms import expand_query_with_synonyms
from tools.gpt_fallback import ask_gpt_policy_helper  # Optional, skip if not ready

def process_policy_query(user_query, index, documents, use_gpt_fallback=True):
    """
    Handles query routing: original → synonym → GPT fallback
    """
    original_query = user_query
    expanded_query = expand_query_with_synonyms(user_query)

    # Try original query
    results = get_top_rag_results(original_query, index, documents)
    if results and not "error" in results[0] and results[0]["score"] > 0.75:
        return {
            "method_used": "RAG",
            "citation_info": results,
            "raw_answer": results[0]["content"]
        }

    # Try synonym-expanded query
    results = get_top_rag_results(expanded_query, index, documents)
    if results and not "error" in results[0] and results[0]["score"] > 0.75:
        return {
            "method_used": "Synonym",
            "citation_info": results,
            "raw_answer": results[0]["content"]
        }

    # GPT fallback (optional)
    if use_gpt_fallback:
        gpt_answer = ask_gpt_policy_helper(user_query)
        return {
            "method_used": "GPT",
            "citation_info": "No citation available",
            "raw_answer": gpt_answer
        }

    # Total miss
    return {
        "method_used": "Miss",
        "citation_info": "No results",
        "raw_answer": "No matching policy found."
    }
