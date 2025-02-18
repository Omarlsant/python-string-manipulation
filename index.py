# Step 55: Calling caesar() without the required arguments stops the execution of the code. Give message and offset values, by passing text and shift as arguments to the caesar function call.

text = 'Hello Zaira'
shift = 3
def caesar(message, offset):
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

caesar(text, shift)