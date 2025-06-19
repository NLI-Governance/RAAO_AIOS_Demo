def load_test_questions(limit=None):
    """
    Loads 100 benchmark policy questions for RAG and GPT validation.
    Use limit=N to run fewer (e.g. limit=25 for quick test).
    """
    full_question_list = [
        {"id": 1, "question": "How do I report workplace harassment?"},
        {"id": 2, "question": "What happens if I’m late three times in a week?"},
        {"id": 3, "question": "Do I get paid for jury duty?"},
        {"id": 4, "question": "Who approves my paid time off request?"},
        {"id": 5, "question": "How do I file a grievance or complaint?"},
        {"id": 6, "question": "When does my health insurance start after being hired?"},
        {"id": 7, "question": "Is there a dress code I need to follow?"},
        {"id": 8, "question": "What’s the process for requesting a schedule change?"},
        {"id": 9, "question": "Do we have safety protocols for field work?"},
        {"id": 10, "question": "How do I access my training records?"},
        # ... (questions 11 through 100 follow same structure)
        {"id": 100, "question": "Is verbal abuse considered a violation of policy?"}
    ]

    return full_question_list if limit is None else full_question_list[:limit]
