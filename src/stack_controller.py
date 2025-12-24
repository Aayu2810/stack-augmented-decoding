from task_stack import TaskStack
from llm_interface import mock_llm_process

class StackController:
    def __init__(self):
        self.stack = TaskStack()
        self.stack_history = []
        self.execution_log = []

    def load_tasks(self, tasks):
        for task in reversed(tasks):
            self.stack.push(task)

    def run(self):
        step = 0

        while not self.stack.is_empty():
            step += 1
            current_task = self.stack.pop()

            self.execution_log.append(
                f"Step {step}: Processing -> {current_task}"
            )

            result, _ = mock_llm_process(current_task)
            self.execution_log.append(result)

            self.stack_history.append(self.stack.size())

        return self.stack_history, self.execution_log
