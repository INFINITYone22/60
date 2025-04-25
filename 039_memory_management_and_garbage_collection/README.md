# Project Title: Memory Management and Garbage Collection

## Description
This project explores memory usage and cleanup in Python.

## Learning Objectives
- Understand how memory is managed in Python.
- Learn how to use the `gc` module to control garbage collection.
- Explore memory usage and cleanup techniques.

## Prerequisites
- Python installed on your system.
- Basic knowledge of memory management and garbage collection.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `gc` and `sys` modules.
- It creates a large list to allocate a significant amount of memory.
- It uses `sys.getsizeof()` to get the size of the list in bytes.
- It deletes the list using `del`.
- It calls `gc.collect()` to force garbage collection.
- It prints the number of unreachable objects collected by the garbage collector.

## Extensions
- Add more complex memory management scenarios.
- Implement a GUI using Tkinter.
- Allow the user to control the garbage collection settings.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
