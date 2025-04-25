# Project Title: Statistical Analysis with SciPy

## Description
This project performs statistical tests using SciPy.

## Learning Objectives
- Understand how to use the `scipy.stats` module in Python.
- Learn how to perform t-tests and normality tests.

## Prerequisites
- Python installed on your system.
- Basic knowledge of statistics and the `scipy.stats` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `numpy` and `scipy` libraries using the command `pip install numpy scipy`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `numpy` and `scipy.stats` modules.
- It generates two sample datasets using `np.random.normal()`.
- It performs an independent samples t-test using `stats.ttest_ind()`.
- It performs a Shapiro-Wilk test for normality using `stats.shapiro()`.
- It prints the test statistics and p-values to the console.

## Extensions
- Add more statistical tests, such as ANOVA or chi-squared tests.
- Implement a GUI using Tkinter.
- Allow the user to specify the data and the statistical tests to be performed.

## References
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Real Python](https://realpython.com/)
