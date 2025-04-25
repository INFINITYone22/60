def is_palindrome(text):
    processed_text = ''.join(text.lower().split())
    return processed_text == processed_text[::-1]

text = input("Enter a word or phrase: ")
if is_palindrome(text):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
