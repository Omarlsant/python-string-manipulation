# Step 62: Next, inside the else block, declare a variable called key_char and assign it the value of key at the index key_index mod(%) the length of key.

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
            key_char = key[key_index % len(key)]
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
            
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
