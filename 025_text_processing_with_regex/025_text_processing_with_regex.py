import re

def text_processing_with_regex(text):
    # Find all email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    print("Email addresses:", emails)

    # Find all phone numbers (basic format)
    phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    print("Phone numbers:", phone_numbers)

    # Find all words starting with 'a'
    words_with_a = re.findall(r"\ba\w+", text, re.IGNORECASE)
    print("Words starting with 'a':", words_with_a)

text = input("Enter some text: ")
text_processing_with_regex(text)
