import re
s=str(input())
pattern="[A-Z][a-z]+"
x=re.findall(pattern, s)
print(x)