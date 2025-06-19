from tools.query_policy_rag_core import get_top_rag_results
from tools.query_policy_rag_synonyms import expand_query_with_synonyms
import openai

def ask_gpt_to_summarize_chunk(user_query, rag_chunk):
    """
    Given a RAG match and the original question, ask GPT to explain it simply.
    """
    prompt = f"""A user asked: "{user_query}"

Here is a policy section that may be relevant:

--- POLICY START ---
{rag_chunk}
--- POLICY END ---

Please summarize the above clearly and concisely for the user. Avoid legal language and do not make up details not found in the text."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful HR policy assistant. Use only the provided policy text to explain answers."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except openai.error.RateLimitError:
        return "(GPT summarization unavailable due to quota limits.)"
    except Exception as e:
        return f"(Error generating GPT summary: {str(e)})"

def ask_gpt_policy_fallback(user_query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful HR policy assistant. Provide respectful answers based on typical best practices."},
                {"role": "user", "content": user_query}
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except openai.error.RateLimitError:
        return "(GPT fallback unavailable due to quota limits.)"
    except Exception as e:
        return f"(Error with GPT fallback: {str(e)})"

def process_policy_query(user_query, index, documents, use_gpt_fallback=True):
    """
    Main assistant logic: original → synonym → GPT fallback.
    GPT is also used to summarize RAG hits.
    """
    original_query = user_query
    expanded_query = expand_query_with_synonyms(user_query)

    # Try original RAG
    results = get_top_rag_results(original_query, index, documents)
    if results and not "error" in results[0] and results[0]["score"] > 0.75:
        top_chunk = results[0]["content"]
        summary = ask_gpt_to_summarize_chunk(user_query, top_chunk)
        return {
            "method_used": "RAG",
            "citation_info": results,
            "raw_answer": summary
        }

    # Try synonym match
    results = get_top_rag_results(expanded_query, index, documents)
    if results and not "error" in results[0] and results[0]["score"] > 0.75:
        top_chunk = results[0]["content"]
        summary = ask_gpt_to_summarize_chunk(user_query, top_chunk)
        return {
            "method_used": "Synonym",
            "citation_info": results,
            "raw_answer": summary
        }

    # Fallback to GPT if allowed
    if use_gpt_fallback:
        gpt_answer = ask_gpt_policy_fallback(user_query)
        return {
            "method_used": "GPT",
            "citation_info": "No citation available",
            "raw_answer": gpt_answer
        }

    return {
        "method_used": "Miss",
        "citation_info": "No results",
        "raw_answer": "No matching policy found."
    }
