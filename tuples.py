import math
a=(6,4,3)
b=(8,1,2)
res=[]
for i in range(0,len(a)):
    res.append(a[i]-b[i])
res=tuple(res) 
print(res)
dis=(math.sqrt(res[0]*res[0]+res[1]*res[1]+res[2]*res[2]))
print(dis)



