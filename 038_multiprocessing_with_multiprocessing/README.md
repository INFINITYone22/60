# Project Title: Multiprocessing with Multiprocessing

## Description
This project parallelizes a computation-heavy task using multiprocessing.

## Learning Objectives
- Understand how to use the `multiprocessing` module in Python.
- Learn how to create and start processes.
- Implement parallel programming using multiprocessing.

## Prerequisites
- Python installed on your system.
- Basic knowledge of multiprocessing and the `multiprocessing` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `multiprocessing` and `time` modules.
- It defines a function `square(n)` that calculates the square of a number and sleeps for 1 second to simulate a long computation.
- It defines a function `main()` that creates a pool of processes using `multiprocessing.Pool()`.
- It uses the `pool.map()` method to apply the `square()` function to each number in a list.
- The `pool.map()` method automatically distributes the tasks to the available processes.
- The program prints the squared numbers to the console.

## Extensions
- Add more complex computations to the `square()` function.
- Implement a GUI using Tkinter.
- Allow the user to specify the number of processes to use.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
