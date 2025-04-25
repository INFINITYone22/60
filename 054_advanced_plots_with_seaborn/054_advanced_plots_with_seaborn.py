import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def advanced_plots_with_seaborn():
    # Generate some sample data
    np.random.seed(42)
    data = pd.DataFrame({'x': np.random.randn(100),
                         'y': np.random.randn(100),
                         'category': np.random.choice(['A', 'B', 'C'], 100)})

    # Create a scatter plot with different colors for each category
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='x', y='y', hue='category', data=data)
    plt.title("Scatter Plot with Categories")
    plt.savefig("seaborn_scatter.png")
    print("Seaborn scatter plot saved to seaborn_scatter.png")

    # Create a distribution plot
    plt.figure(figsize=(8, 6))
    sns.histplot(data['x'], kde=True)
    plt.title("Distribution of X")
    plt.savefig("seaborn_distribution.png")
    print("Seaborn distribution plot saved to seaborn_distribution.png")

advanced_plots_with_seaborn()
