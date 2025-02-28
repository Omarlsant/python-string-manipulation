# Step 84: Delete the pass keyword, and return vigenere(message, key) from your new function.

text = 'Hello Zaira!'
custom_key = 'python'
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
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

def encrypt(message, key):
    return vigenere(message, key)

encryption = vigenere(text, custom_key)
print(encryption)
decryption = vigenere(encryption, custom_key)
print(decryption)