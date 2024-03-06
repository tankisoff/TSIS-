import re
s=str(input())
x=re.split('_', s)
res=x[0]
for i in range(1,len(x)):
    res+=x[i].capitalize()

print(res)