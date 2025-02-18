# Step 59: Delete your shift variable. Then, declare a new variable called custom_key and assign the value of the string 'python' to this variable.

text = 'Hello Zaira'
custom_key = 'python'
def vigenere(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
