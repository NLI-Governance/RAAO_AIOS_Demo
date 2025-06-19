def get_top_rag_results(query, index, documents, top_k=3):
    """
    Performs vector similarity search and returns structured results.
    Assumes index supports similarity_search_with_score.
    """
    try:
        results = index.similarity_search_with_score(query, k=top_k)
        structured_results = []

        for doc, score in results:
            doc_name = doc.metadata.get("source", "Unknown Document")
            line_range = doc.metadata.get("lines", "Unknown Lines")
            section = doc.metadata.get("section", "Unspecified Section")

            structured_results.append({
                "document": doc_name,
                "section": section,
                "lines": line_range,
                "score": round(score, 4),
                "content": doc.page_content
            })

        return structured_results

    except Exception as e:
        return [{"error": str(e)}]
