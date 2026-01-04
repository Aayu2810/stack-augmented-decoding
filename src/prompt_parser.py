def parse_prompt(prompt_data):
    """
    Takes structured prompt input and returns subtasks.
    """
    return prompt_data.get("subtasks", [])

