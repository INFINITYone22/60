# Project Title: Basic File Reader/Writer

## Description
This project reads from and writes to a text file.

## Learning Objectives
- Understand how to open and close files in Python.
- Learn how to read from and write to files.
- Implement error handling for file operations.

## Prerequisites
- Python installed on your system.
- Basic knowledge of file operations and functions.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the file reader/writer in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.
5.  Enter the filename and action (read or write) when prompted.
6.  If writing, enter the text to write to the file.

## Code Explanation
- The program defines a function `file_reader_writer(filename, text=None)` that takes a filename and optional text as input.
- If text is None, it opens the file in read mode and returns the content.
- If text is not None, it opens the file in write mode and writes the text to the file.
- It includes error handling for FileNotFoundError.

## Extensions
- Add error handling for other file-related errors.
- Allow the user to specify the file encoding.
- Implement a GUI using Tkinter.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
