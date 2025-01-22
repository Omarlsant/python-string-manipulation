# Step 45: Surround index + shift with parentheses, and modulo the expression with 26, which is the alphabet length.

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % 26
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)
