# Project Title: Basic Networking with Sockets

## Description
This project creates a simple client-server chat program using sockets.

## Learning Objectives
- Understand how to use the `socket` module in Python.
- Learn how to create a server and a client.
- Implement basic networking communication.

## Prerequisites
- Python installed on your system.
- Basic knowledge of the `socket` module and networking concepts.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the server using the command `python server.py`.
5.  Open another terminal or command prompt.
6.  Navigate to the project directory.
7.  Run the client using the command `python client.py`.

## Code Explanation
- The project consists of two files: `server.py` and `client.py`.
- The `server.py` file creates a server socket, listens for incoming connections, and exchanges messages with the client.
- The `client.py` file creates a client socket, connects to the server, and exchanges messages with the server.
- The `socket` module is used to create and manage the sockets.
- The `HOST` and `PORT` variables define the server's address and port.

## Extensions
- Add more features, such as multiple clients or a GUI.
- Implement error handling for network errors.
- Use a different protocol, such as UDP.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
