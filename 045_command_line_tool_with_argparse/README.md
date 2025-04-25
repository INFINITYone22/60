# Project Title: Command-Line Tool with Argparse

## Description
This project builds a CLI tool with multiple options using the `argparse` module.

## Learning Objectives
- Understand how to use the `argparse` module in Python.
- Learn how to define command-line arguments and options.
- Implement a CLI tool with multiple options.

## Prerequisites
- Python installed on your system.
- Basic knowledge of command-line arguments and the `argparse` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the program using the command `python main.py <name> [-a <age>] [-v]`.

## Code Explanation
- The program imports the `argparse` module.
- It creates an `ArgumentParser` object with a description.
- It adds arguments using `parser.add_argument()`.
- It parses the arguments using `parser.parse_args()`.
- It prints a greeting message based on the arguments.
- It prints verbose output if the `-v` or `--verbose` option is specified.

## Extensions
- Add more arguments and options to the CLI tool.
- Implement different actions based on the arguments.
- Add error handling for missing or invalid arguments.

## References
- [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [Real Python](https://realpython.com/)
