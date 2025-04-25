# Project Title: Grouping and Aggregating Data

## Description
This project analyzes data by groups using Pandas.

## Learning Objectives
- Understand how to use Pandas for grouping and aggregating data in DataFrames.
- Learn how to use the `groupby()` method.
- Learn how to use aggregation functions like `mean()`, `sum()`, and `count()`.

## Prerequisites
- Python installed on your system.
- Basic knowledge of Pandas DataFrames.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `pandas` library using the command `pip install pandas`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `pandas` module as `pd`.
- It creates a sample DataFrame with data about employees in different departments.
- It groups the DataFrame by the 'Department' column using `df.groupby()`.
- It calculates the mean salary for each department using `grouped_df['Salary'].mean()`.
- It calculates the sum and count of salaries for each department using `grouped_df['Salary'].agg(['sum', 'count'])`.

## Extensions
- Add more complex grouping and aggregation scenarios.
- Implement a GUI using Tkinter.
- Allow the user to specify the DataFrame, the grouping column, and the aggregation functions.

## References
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Real Python](https://realpython.com/)
