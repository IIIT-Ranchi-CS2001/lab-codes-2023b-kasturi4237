n=int(input("ENTER THE NUMBER :"))
n1=int(input("ENTER THE LIMIT UPTO TO WHICH THE TABLE IS TO BE PRINTED :"))

for i in range(n1):
  print(f"{n}  *  {i+1}  = ",n*(i+1))
  i+=1
