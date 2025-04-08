import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_over_heatmap(df):
    heatmap_data = df.pivot(index="match_id", columns="over", values="runs")
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.5)
    plt.title("Runs per Over (Match-wise)")
    plt.xlabel("Over")
    plt.ylabel("Match ID")
    plt.tight_layout()
    plt.savefig("over_heatmap.png")