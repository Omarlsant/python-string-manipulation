# Step 67: Remove the two print() calls from your function and return encrypted_text.

text = 'Hello Zaira'
custom_key = 'python'
def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
        # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text
