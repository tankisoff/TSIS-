import re
s=str(input())
patterns = 'ab{2,3}'
x=re.findall(patterns, s)
print(x)