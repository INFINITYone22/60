def caesar_cipher(text, shift, action):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

text = input("Enter text: ")
shift = int(input("Enter shift value: "))
action = input("Encrypt (e) or Decrypt (d)? ")

if action.lower() == 'e':
    print("Encrypted:", caesar_cipher(text, shift, 'e'))
elif action.lower() == 'd':
    print("Decrypted:", caesar_cipher(text, -shift, 'd'))
else:
    print("Invalid action.")
