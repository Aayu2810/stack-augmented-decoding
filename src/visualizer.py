import matplotlib.pyplot as plt

def plot_stack_height(stack_history, output_path):
    steps = list(range(1, len(stack_history) + 1))

    plt.figure()
    plt.bar(steps, stack_history)
    plt.xlabel("Reasoning Step")
    plt.ylabel("Stack Height")
    plt.title("Stack Height Over Time During LLM Reasoning")

    plt.savefig(output_path)
    plt.close()

