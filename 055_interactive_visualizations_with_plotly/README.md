# Project Title: Interactive Visualizations with Plotly

## Description
This project builds an interactive chart using Plotly.

## Learning Objectives
- Understand how to use the `plotly.express` module in Python.
- Learn how to create interactive scatter plots and histograms with Plotly.

## Prerequisites
- Python installed on your system.
- Basic knowledge of data visualization and the `plotly.express` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `plotly`, `pandas`, and `numpy` libraries using the command `pip install plotly pandas numpy`.
5.  Run the program using the command `python main.py`.
6.  Open the generated HTML files (plotly_scatter.html and plotly_histogram.html) in your browser to view the interactive plots.

## Code Explanation
- The program imports the `plotly.express`, `pandas`, and `numpy` modules.
- It generates sample data using `np.random.randn()` and `np.random.choice()`.
- It creates an interactive scatter plot using `px.scatter()` and saves it to an HTML file using `fig.write_html()`.
- It creates an interactive histogram using `px.histogram()` and saves it to an HTML file using `fig.write_html()`.

## Extensions
- Add more plot types, such as 3D scatter plots or choropleth maps.
- Allow the user to specify the data and the plot types to be created.

## References
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Real Python](https://realpython.com/)
