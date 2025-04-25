# Project Title: Geospatial Data Analysis

## Description
This project visualizes geographic data using GeoPandas.

## Learning Objectives
- Understand how to use the `geopandas` module in Python.
- Learn how to load and plot shapefiles.
- Filter geospatial data.

## Prerequisites
- Python installed on your system.
- Basic knowledge of geospatial data and GeoPandas.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `geopandas`, `matplotlib`, and `fiona` libraries using the command `pip install geopandas matplotlib fiona`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `geopandas` and `matplotlib.pyplot` modules.
- It loads a shapefile using `gpd.read_file()`.
- It filters the data to only include countries in Africa.
- It plots the map of Africa using `africa.plot()`.

## Extensions
- Add more complex geospatial analysis techniques, such as calculating distances or performing spatial joins.
- Implement a GUI using Tkinter.
- Allow the user to specify the shapefile and the analysis operations to be performed.

## References
- [GeoPandas Documentation](https://geopandas.org/en/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
- [Real Python](https://realpython.com/)
