# String manipulation
S1 = "Maha Bharat"

# Required transformations
print(S1.swapcase())
print(S1[5:])
print(S1[5:] * 3)
print("Mera " + S1[5:])
print("Mera " + S1[5:] + " Mahan")

# String S manipulations
S = "Ba Ba Black Sheep"
print(f"Length of S: {len(S)}")
print(f"First occurrence of 'e': {S.find('e')}")
print(f"Total occurrences of 'a': {S.count('a')}")
print(S.replace("Ba", "Ta", 1))
