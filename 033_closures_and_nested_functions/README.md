# Project Title: Closures and Nested Functions

## Description
This project implements a counter using closures and nested functions.

## Learning Objectives
- Understand how to define nested functions in Python.
- Learn how to use closures to capture and retain state.
- Implement a counter using closures.

## Prerequisites
- Python installed on your system.
- Basic knowledge of functions, nested functions, and closures.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the closures and nested functions in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program defines a function `counter()` that returns a nested function `increment()`.
- The `increment()` function uses the `nonlocal` keyword to modify the `count` variable in the outer scope.
- The `counter()` function returns the `increment()` function, which captures the `count` variable in its closure.
- Each call to the returned `increment()` function increments the `count` variable and returns the new value.

## Extensions
- Add more features to the counter, such as decrementing or resetting the count.
- Implement a GUI using Tkinter.
- Allow the user to specify the initial count value.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
