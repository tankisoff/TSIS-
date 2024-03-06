import re
import string

s=str(input())

x=re.split('_', s)
print(x)
result=[]
for i in range(len(x)-1):
    if x[i].islower() and x[i+1].islower():
        result.append(f"{x[i]}_{x[i+1]}")
print(result)