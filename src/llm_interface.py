def mock_llm_process(task):
    """
    Simulates LLM processing a task.
    Returns result text and optional new subtasks.
    """

    result = f"Completed task: {task}"
    new_subtasks = []

    # Generate subtasks ONLY once to avoid infinite recursion
    if task == "Solve main problem":
        new_subtasks = [
            "Break down main problem",
            "Execute main problem"
        ]

    return result, new_subtasks
