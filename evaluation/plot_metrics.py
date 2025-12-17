import matplotlib.pyplot as plt
import json
import os

def plot_improvement(metrics_history_path: str):
    """Generates a PNG plot showing the learning curve of the agent."""
    if not os.path.exists(metrics_history_path):
        print("No history file found to plot.")
        return

    with open(metrics_history_path, 'r') as f:
        data = json.load(f) # List of dicts from evaluation/evaluate_agent.py

    iterations = range(1, len(data) + 1)
    precision = [d['Verified Bug Precision'] for d in data]
    fp_rate = [d['False Positive Rate'] for d in data]

    plt.figure(figsize=(10, 5))
    
    plt.plot(iterations, precision, marker='o', label='Precision (%)', color='green')
    plt.plot(iterations, fp_rate, marker='s', label='False Positive Rate (%)', color='red')

    plt.title('Agent Learning Curve: Precision vs False Positives')
    plt.xlabel('Iteration (Batch of PRs)')
    plt.ylabel('Percentage')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.savefig('performance_trend.png')
    plt.show()
    print("Plot saved as performance_trend.png")
