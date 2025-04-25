# Project Title: Unit Testing with unittest

## Description
This project demonstrates how to write unit tests for a simple function using the `unittest` module.

## Learning Objectives
- Understand how to use the `unittest` module in Python.
- Learn how to write test cases and assertions.
- Implement unit testing for a simple function.

## Prerequisites
- Python installed on your system.
- Basic knowledge of unit testing and the `unittest` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the unit testing in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `unittest` module.
- It defines a function `add(x, y)` that adds two numbers.
- It defines a class `TestAdd(unittest.TestCase)` that inherits from `unittest.TestCase`.
- It defines test methods `test_add_positive_numbers()`, `test_add_negative_numbers()`, and `test_add_mixed_numbers()` that test the `add()` function with different inputs.
- It uses the `self.assertEqual()` method to assert that the actual result is equal to the expected result.
- The `if __name__ == '__main__':` block runs the unit tests when the script is executed.

## Extensions
- Add more test cases to cover different scenarios.
- Implement unit testing for more complex functions.
- Use a test runner to run the unit tests.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
