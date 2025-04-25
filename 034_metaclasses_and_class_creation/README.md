# Project Title: Metaclasses and Class Creation

## Description
This project creates a custom metaclass that adds an attribute to a class during class creation.

## Learning Objectives
- Understand how to define metaclasses in Python.
- Learn how to use the `__new__` method to customize class creation.
- Implement metaclasses to modify class attributes.

## Prerequisites
- Python installed on your system.
- Basic knowledge of classes, objects, and metaclasses.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the metaclasses and class creation in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program defines a metaclass `MyMeta` that inherits from `type`.
- The `__new__` method of `MyMeta` is called when a class is created using this metaclass.
- The `__new__` method adds an attribute named `attribute` with the value `'Custom attribute'` to the class.
- The program defines a class `MyClass` that uses the `MyMeta` metaclass.
- The program creates an instance of `MyClass` and prints the value of the `attribute` attribute.

## Extensions
- Add more complex logic to the metaclass to modify class behavior in different ways.
- Implement a GUI using Tkinter.
- Allow the user to specify the attributes to be added to the class.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
