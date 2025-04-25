# Project Title: Simple Encryption/Decryption

## Description
This project implements a basic Caesar cipher for encryption and decryption.

## Learning Objectives
- Understand how to define functions in Python.
- Learn how to manipulate strings in Python.
- Implement basic encryption and decryption techniques.

## Prerequisites
- Python installed on your system.
- Basic knowledge of strings, functions, and encryption concepts.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the encryption/decryption in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.
5.  Enter the text, shift value, and action (encrypt or decrypt) when prompted.

## Code Explanation
- The program defines a function `caesar_cipher(text, shift, action)` that takes the text, shift value, and action as input.
- It iterates over each character in the text.
- If the character is an alphabet, it shifts the character by the shift value.
- If the character is a digit, it shifts the digit by the shift value.
- Otherwise, it keeps the character as is.
- It returns the encrypted or decrypted text.

## Extensions
- Implement more advanced encryption algorithms.
- Handle special characters and non-ASCII characters.
- Implement a GUI using Tkinter.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
