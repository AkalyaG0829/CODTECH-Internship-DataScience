import matplotlib.pyplot as plt
import os

def plot_production(plan, save_path="reports/figures/production_plan.png", show=False):
    """Plot the optimal production plan as a bar chart."""
    products = list(plan.keys())
    values = [plan[p] for p in products]

    plt.figure(figsize=(7,5))
    plt.bar(products, values, color=["#4c9", "#e55", "#f9a", "#6cf", "#fc3"])
    plt.title("Optimal Production Plan")
    plt.xlabel("Product")
    plt.ylabel("Units")
    plt.tight_layout()

    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.savefig(save_path)

    if show:   # <-- this part makes the chart visible inline
        plt.show()

    plt.close()