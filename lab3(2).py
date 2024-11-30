n=int(input("ENTER THE NUMBER :"))
res=0
n1=n
while n>0:
  s=n%10
  res+=s
  n=n//10
print(f"the sum of the digits of the number {n1} is",res)
   

