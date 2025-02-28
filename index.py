# Step 79: Right now, punctuation, special characters or digits are not encoded/decoded correctly. Check this by adding an exclamation mark at the end of the text string.

text = 'Hello Zaira!'
custom_key = 'python'
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        # Append space to the message
        if char == ' ':
            final_message += char
        else:
        # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

encryption = vigenere(text, custom_key)
print(encryption)
decryption = vigenere(encryption, custom_key)
print(decryption)