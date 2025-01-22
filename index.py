# Step 41: At the top of your for loop, replace print(char == ' ') with an if statement. The condition of this if statement should evaluate to True if char is an empty space and False otherwise. Inside the if body, print the string 'space!'. Remember to indent this line.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    if char == ' ':
        print('space!')
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)
