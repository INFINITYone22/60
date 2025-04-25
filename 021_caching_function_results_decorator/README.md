# Project Title: Caching Function Results (Decorator)

## Description
This project caches the results of a function using a decorator to improve performance.

## Learning Objectives
- Understand how to define functions in Python.
- Learn how to use decorators to modify function behavior.
- Implement caching to store and retrieve function results.

## Prerequisites
- Python installed on your system.
- Basic knowledge of functions, decorators, and dictionaries.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the caching function results in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program defines a function `cache(func)` that acts as a decorator.
- The `cache` function creates a dictionary `cached_results` to store the results.
- The `wrapper` function checks if the result for the given arguments is already cached.
- If the result is cached, it returns the cached result.
- Otherwise, it calls the original function, caches the result, and returns it.
- The `@cache` syntax applies the decorator to the `expensive_function`.

## Extensions
- Add more sophisticated caching strategies, such as LRU or TTL.
- Implement a GUI using Tkinter.
- Allow the user to specify the function to be cached.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
