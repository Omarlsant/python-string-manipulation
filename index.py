# Step 47: Next, modify your print() call to print 'encrypted text:', encrypted_text and put it outside the for loop, so that the encrypted string is printed one time.

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]
print('encrypted text:', encrypted_text)
