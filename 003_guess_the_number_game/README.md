# Project Title: Guess the Number Game

## Description
This project is a number guessing game where the user tries to guess a randomly generated number between 1 and 100. The program provides hints to the user, indicating whether their guess is too low or too high.

## Learning Objectives
- Understand how to generate random numbers in Python.
- Learn how to take user input and validate it.
- Implement a `while` loop for repeated guessing.
- Use conditional statements to provide hints.

## Prerequisites
- Python installed on your system.
- Basic knowledge of variables, loops, and conditional statements.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.

## Implementation Steps
1.  Create a file named `main.py`.
2.  Write the code for the guess the number game in the file.
3.  Save the file.
4.  Run the program using the command `python main.py`.
5.  Follow the prompts to enter your guess.

## Code Explanation
- The program uses the `random.randint()` function to generate a random number between 1 and 100.
- It uses a `while` loop to repeatedly ask the user for a guess until they guess the correct number.
- It uses `if` and `elif` statements to provide hints to the user.
- It uses a `try-except` block to handle potential `ValueError` exceptions if the user enters non-numeric input.

## Extensions
- Allow the user to choose the range of numbers.
- Limit the number of tries the user can take.
- Keep track of the user's high score.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
