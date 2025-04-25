# Project Title: Data Visualization with Matplotlib

## Description
This project creates basic plots (e.g., bar, line) using Matplotlib.

## Learning Objectives
- Understand how to use the `matplotlib.pyplot` module in Python.
- Learn how to create line plots and scatter plots.
- Customize plot appearance with titles, labels, and grids.

## Prerequisites
- Python installed on your system.
- Basic knowledge of data visualization and the `matplotlib.pyplot` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `matplotlib` and `numpy` libraries using the command `pip install matplotlib numpy`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `matplotlib.pyplot` module as `plt` and the `numpy` module as `np`.
- It generates sample data using `np.linspace()` and `np.random.rand()`.
- It creates a line plot using `plt.plot()` and customizes the plot with `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, and `plt.grid()`.
- It creates a scatter plot using `plt.scatter()` and customizes the plot with colors, sizes, and a colorbar.
- It saves the plots to PNG files using `plt.savefig()`.

## Extensions
- Add more plot types, such as bar charts or histograms.
- Implement a GUI using Tkinter.
- Allow the user to specify the data and the plot types to be created.

## References
- [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
- [Real Python](https://realpython.com/)
