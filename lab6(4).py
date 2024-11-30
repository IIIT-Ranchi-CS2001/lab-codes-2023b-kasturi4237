import re

# User input string
input_string = "Tom 25 Rahu22 2@$"

# Find all letters and convert to uppercase
letters = list(filter(lambda x: x.isalpha(), input_string.split()))
uppercase_letters = list(map(lambda x: x.upper(), letters))
print("Letters in uppercase:", uppercase_letters)

# Find all digits and compute their squares
digits = list(filter(lambda x: x.isdigit(), input_string.split()))
squares = list(map(lambda x: int(x)**2, digits))
print("Squares of digits:", squares)

# Find all alphanumeric strings
alphanumeric = list(filter(lambda x: re.match(r"^[a-zA-Z0-9]+$", x), input_string.split()))
print("Alphanumeric characters:", alphanumeric)
