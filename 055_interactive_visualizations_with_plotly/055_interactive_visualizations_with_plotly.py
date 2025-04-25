import plotly.express as px
import pandas as pd
import numpy as np

def interactive_visualizations_with_plotly():
    # Generate some sample data
    np.random.seed(42)
    data = pd.DataFrame({'x': np.random.randn(100),
                         'y': np.random.randn(100),
                         'category': np.random.choice(['A', 'B', 'C'], 100)})

    # Create an interactive scatter plot
    fig = px.scatter(data, x='x', y='y', color='category',
                     title='Interactive Scatter Plot')
    fig.write_html("plotly_scatter.html")
    print("Plotly scatter plot saved to plotly_scatter.html")

    # Create an interactive histogram
    fig = px.histogram(data, x='x', color='category',
                       title='Interactive Histogram')
    fig.write_html("plotly_histogram.html")
    print("Plotly histogram saved to plotly_histogram.html")

interactive_visualizations_with_plotly()
