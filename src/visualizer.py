import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_stack_height(stack_history, output_path):
    if not stack_history:
        return

    steps = range(1, len(stack_history) + 1)

    plt.figure()
    plt.plot(steps, stack_history, marker="o")
    plt.xlabel("Step")
    plt.ylabel("Stack Height")
    plt.title("Stack Height During Reasoning")
    plt.savefig(output_path)
    plt.close()
