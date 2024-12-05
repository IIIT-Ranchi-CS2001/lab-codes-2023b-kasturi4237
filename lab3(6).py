str=input("ENTER THE STRING  : ")
c=input("enter the character to find  : ")
i=0
count=0
for i in str:
    if i==c:
        count=count+1
          
print(f"THE NUMBER OF OCCURANCE OF THE CHARACTER IS {c} is  :   ",count)    