str=(input("ENTER THE SENTENCE : "))
count=0
words=str.split()
for i in words:
    if i== i[::-1]:
        count +=1
print("THE NUMBER OF PALINDROME WORDS IS :  ",count)


