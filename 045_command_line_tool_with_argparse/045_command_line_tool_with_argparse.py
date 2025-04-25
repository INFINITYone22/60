import argparse

def command_line_tool_with_argparse():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    parser.add_argument("name", help="The name to greet.")
    parser.add_argument("-a", "--age", type=int, help="Your age.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()

    greeting = f"Hello, {args.name}!"
    if args.age:
        greeting += f" You are {args.age} years old."

    print(greeting)

    if args.verbose:
        print("This is verbose output.")

if __name__ == "__main__":
    command_line_tool_with_argparse()
