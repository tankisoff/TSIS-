import re
s=str(input())
x=re.findall('[A-Z][^A-Z]*', s)
for i in x:
    print(i +" ", end='')
