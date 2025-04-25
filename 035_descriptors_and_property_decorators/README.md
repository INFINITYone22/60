# Project Title: Descriptors and Property Decorators

## Description
This project manages attribute access with descriptors.

## Learning Objectives
- Understand how to define descriptors in Python.
- Learn how to use the `__get__`, `__set__`, and `__delete__` methods to customize attribute access.
- Implement property decorators to simplify descriptor creation.

## Prerequisites
- Python installed on your system.
- Basic knowledge of classes, objects, and descriptors.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the descriptors and property decorators in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program defines a descriptor class `Temperature` with `__get__` and `__set__` methods.
- The `__get__` method returns the temperature value.
- The `__set__` method validates the temperature value and raises a `ValueError` if it is below absolute zero.
- The program defines a class `Thermometer` that uses the `Temperature` descriptor for its `temperature` attribute.
- The program creates an instance of `Thermometer` and demonstrates how to access and modify the `temperature` attribute.

## Extensions
- Add more complex validation logic to the `__set__` method.
- Implement a GUI using Tkinter.
- Allow the user to specify the temperature range.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
