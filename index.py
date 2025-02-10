# Step 53: Modify your function declaration so that it takes two parameters called message and offset. After that, you'll see an error appear in the terminal. 

text = 'Hello Zaira'
shift = 3
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)

caesar()