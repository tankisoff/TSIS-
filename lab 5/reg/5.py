import re
s=str(input())
pattern = 'a[^ b]*b'
x=re.findall(pattern, s)
print(x)
