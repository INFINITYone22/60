# Project Title: Prime Number Checker

## Description
This project determines whether a number entered by the user is a prime number or not.

## Learning Objectives
- Understand how to define functions in Python.
- Learn how to use loops in Python.
- Implement conditional statements.

## Prerequisites
- Python installed on your system.
- Basic knowledge of numbers, loops, and functions.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the prime number checker in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.
5.  Enter a number when prompted.

## Code Explanation
- The program defines a function `is_prime(number)` that takes an integer as input.
- It checks if the number is less than or equal to 1. If so, it returns `False`.
- It iterates from 2 to the square root of the number.
- For each number in the range, it checks if the input number is divisible by the current number. If so, it returns `False`.
- If the loop completes without finding a divisor, it returns `True`.

## Extensions
- Optimize the prime number checker for larger numbers.
- Generate a list of prime numbers within a given range.
- Implement a GUI using Tkinter.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
