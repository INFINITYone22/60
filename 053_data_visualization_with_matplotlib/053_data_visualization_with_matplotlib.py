import matplotlib.pyplot as plt
import numpy as np

def data_visualization_with_matplotlib():
    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a line plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.savefig("sine_wave.png")
    print("Sine wave plot saved to sine_wave.png")

    # Create a scatter plot
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = np.random.rand(50) * 100

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.colorbar(label="Color Intensity")
    plt.savefig("scatter_plot.png")
    print("Scatter plot saved to scatter_plot.png")

data_visualization_with_matplotlib()
