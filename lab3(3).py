n=int(input("ENTER THE NUMBER OF TERMS : "))
i=2
a=0
b=1
s=0
print(a)
print(b)
while i<n:
   s=a+b
   print(s)
   a=b
   b=s
   i+=1



