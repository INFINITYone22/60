# Project Title: Asynchronous Programming with Asyncio

## Description
This project fetches multiple URLs concurrently using asynchronous programming with Asyncio.

## Learning Objectives
- Understand how to use the `asyncio` module in Python.
- Learn how to define asynchronous functions using `async` and `await`.
- Implement concurrent programming using `asyncio.gather()`.

## Prerequisites
- Python installed on your system.
- Basic knowledge of asynchronous programming and the `asyncio` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `aiohttp` library using the command `pip install aiohttp`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `asyncio` and `aiohttp` modules.
- It defines an asynchronous function `fetch_url(url)` that fetches the content of a URL using `aiohttp`.
- It defines an asynchronous function `main()` that fetches multiple URLs concurrently using `asyncio.gather()`.
- The `asyncio.run(main())` starts the asynchronous event loop.

## Extensions
- Add error handling for network errors.
- Implement a GUI using Tkinter.
- Allow the user to specify the URLs to be fetched.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
