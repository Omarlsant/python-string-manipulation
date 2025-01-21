# Step 30: Strings are immutable, which means they cannot be changed once created. Confirm that by using the bracket notation to access the first letter in text and try to change it into a character of your choice.

text = 'Hello World'
text[0] = 'm'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
