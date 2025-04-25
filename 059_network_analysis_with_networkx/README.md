# Project Title: Network Analysis with NetworkX

## Description
This project analyzes a simple network using NetworkX.

## Learning Objectives
- Understand how to use the `networkx` module in Python.
- Learn how to create and manipulate graphs.
- Calculate network properties, such as degree centrality.
- Visualize networks.

## Prerequisites
- Python installed on your system.
- Basic knowledge of network analysis and the `networkx` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `networkx` and `matplotlib` libraries using the command `pip install networkx matplotlib`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `networkx` and `matplotlib.pyplot` modules.
- It creates a simple graph using `nx.Graph()`.
- It adds edges to the graph using `graph.add_edges_from()`.
- It calculates the degree centrality of each node using `nx.degree_centrality()`.
- It draws the graph using `nx.draw()` and customizes the appearance with node colors, sizes, and font styles.
- It saves the graph to a PNG file using `plt.savefig()`.

## Extensions
- Add more complex network analysis techniques, such as community detection or pathfinding.
- Implement a GUI using Tkinter.
- Allow the user to specify the graph structure and the analysis operations to be performed.

## References
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
- [Real Python](https://realpython.com/)
