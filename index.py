# Step 31: Delete the text[0] line and reassign text the string 'Albatross'.

text = 'Hello World'
text = 'Albatross'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
