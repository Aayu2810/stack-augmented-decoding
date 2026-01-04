def mock_llm_process(task):
    """
<<<<<<< HEAD
    Mock LLM that ONLY processes tasks.
    NO subtask generation (prevents infinite loops).
    """
    result = f"Completed task: {task}"
    return result, []
=======
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
>>>>>>> 73a565866e40957836d6059e854fa58b3611e6c9
