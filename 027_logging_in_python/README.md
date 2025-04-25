# Project Title: Logging in Python

## Description
This project demonstrates how to implement logging to track program execution.

## Learning Objectives
- Understand how to use the `logging` module in Python.
- Learn how to configure logging levels and formats.
- Implement logging to track program execution and errors.

## Prerequisites
- Python installed on your system.
- Basic knowledge of the `logging` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the logging in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.
5.  Check the `app.log` file for the logging output.

## Code Explanation
- The program imports the `logging` module.
- It configures the logging level, filename, filemode, and format using `logging.basicConfig()`.
- It defines a function `divide(x, y)` that divides two numbers and logs the result or error.
- It uses `logging.info()` to log successful division.
- It uses `logging.error()` to log division by zero errors.

## Extensions
- Add more logging levels, such as warning or critical.
- Implement a GUI using Tkinter.
- Allow the user to configure the logging settings.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
