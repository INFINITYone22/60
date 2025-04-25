# Project Title: Data Cleaning and Preprocessing

## Description
This project cleans a messy dataset using Pandas.

## Learning Objectives
- Understand how to use Pandas for data cleaning and preprocessing.
- Learn how to handle missing values.
- Learn how to remove duplicate rows.
- Convert data types.

## Prerequisites
- Python installed on your system.
- Basic knowledge of Pandas DataFrames.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `pandas` and `numpy` libraries using the command `pip install pandas numpy`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `pandas` and `numpy` modules.
- It creates a sample DataFrame with missing values and duplicates.
- It fills missing values in the 'Age' column with the mean age using `df['Age'].fillna()`.
- It removes duplicate rows using `df.drop_duplicates()`.
- It converts the data type of the 'Age' column to integer using `df['Age'].astype(int)`.

## Extensions
- Add more data cleaning and preprocessing techniques, such as outlier removal or data normalization.
- Implement a GUI using Tkinter.
- Allow the user to specify the data cleaning and preprocessing steps to be performed.

## References
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Real Python](https://realpython.com/)
