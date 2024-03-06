import re
# 1

s=str(input())

x=re.findall("ab*", s)

print(x)