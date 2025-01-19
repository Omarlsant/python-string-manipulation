# Step 27: Add a second argument to print(char) so that it prints the character and its index inside the alphabet.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text:
    index = alphabet.find(char)
    print(char, index)
