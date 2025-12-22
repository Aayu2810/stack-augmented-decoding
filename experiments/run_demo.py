import json
import sys
import os

sys.path.append(os.path.abspath("src"))

from prompt_parser import parse_prompt
from stack_controller import StackController
from visualizer import plot_stack_height

# Load prompt
with open("data/sample_prompts.json", "r") as f:
    prompt_data = json.load(f)

tasks = parse_prompt(prompt_data)

controller = StackController()
controller.load_tasks(tasks)

stack_history, execution_log = controller.run()

# Save execution log
with open("outputs/execution_log.txt", "w") as f:
    for line in execution_log:
        f.write(line + "\n")

# Plot visualization
plot_stack_height(stack_history, "outputs/stack_height_plot.png")

print("Demo completed. Outputs saved in /outputs")

