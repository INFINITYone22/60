# Project Title: Custom Iterator

## Description
This project creates a custom iterable class that can be used in a for loop.

## Learning Objectives
- Understand how to define classes and objects in Python.
- Learn how to implement the iterator protocol (`__iter__` and `__next__` methods).
- Create a custom iterable class.

## Prerequisites
- Python installed on your system.
- Basic knowledge of classes, objects, and iterators.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the custom iterator in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program defines a class `MyIterator` that implements the iterator protocol.
- The `__init__` method initializes the data and the index.
- The `__iter__` method returns the iterator object itself.
- The `__next__` method returns the next value in the sequence and raises `StopIteration` when the end is reached.
- The program creates an instance of the `MyIterator` class and iterates over it using a for loop.

## Extensions
- Implement different types of iterators, such as infinite iterators or iterators that skip values.
- Implement a GUI using Tkinter.
- Allow the user to specify the data to be iterated over.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
