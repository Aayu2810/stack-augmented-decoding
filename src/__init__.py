"""
Stack-Augmented Decoding Framework

This package implements a lightweight, external stack-based controller
to assist Large Language Model (LLM) reasoning without modifying
the model's internal decoding mechanisms.

Modules:
- prompt_parser      : Decomposes structured prompts into subtasks
- task_stack         : Stack data structure for task management
- llm_interface      : Mock LLM task processor
- stack_controller   : Core orchestration logic
- visualizer         : Stack height visualization utilities
"""

