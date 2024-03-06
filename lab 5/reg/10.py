import re
str = str(input())

str1 = re.sub('(.)([A-Z])', r'\1_\2', str)
print(str1.lower())



result=''
for i in str:
    if i.isupper():
        result=result+"_"+i.lower()
    else:
        result+=i

print(result)




num=str(input())
pattern= r"[(][0-9]{3}[)] [0-9]{3}-[0-9]{2}-[0-9]{2}"

x=re.findall(pattern, num)
print(x)