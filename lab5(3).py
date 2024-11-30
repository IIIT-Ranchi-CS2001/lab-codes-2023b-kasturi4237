# Input string
user_string = input("Enter a string: ")

# Count characters
char_count = {char: user_string.count(char) for char in set(user_string)}

# Display the count
print("Character counts:", char_count)
