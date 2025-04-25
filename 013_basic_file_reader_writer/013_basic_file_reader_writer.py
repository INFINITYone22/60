def file_reader_writer(filename, text=None):
    if text is None:
        try:
            with open(filename, 'r') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            return "File not found."
    else:
        with open(filename, 'w') as f:
            f.write(text)
        return "File written successfully."

filename = input("Enter the filename: ")
action = input("Read (r) or Write (w)? ")

if action.lower() == 'r':
    content = file_reader_writer(filename)
    print(content)
elif action.lower() == 'w':
    text = input("Enter the text to write: ")
    result = file_reader_writer(filename, text)
    print(result)
else:
    print("Invalid action.")
