import sys

def argument_parser():
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        print("Arguments:", arguments)
    else:
        print("No arguments provided.")

argument_parser()
