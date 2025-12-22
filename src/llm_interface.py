def mock_llm_process(task):
    """
    Simulates LLM processing a task.
    Returns result text and optional new subtasks.
    """

    result = f"Completed task: {task}"

    # Simulate hierarchical reasoning
    new_subtasks = []
    if "Solve" in task:
        new_subtasks = [
            f"Break down {task}",
            f"Execute {task}"
        ]

    return result, new_subtasks

