import json 
 
print(""" 
Interface Status 
================================================================================ 
DN                                                 Description           Speed    MTU 
-------------------------------------------------- --------------------  ------  ------ 
""" 
) 
 
#raw string 
with open(r"C:\Users\Ashim\Documents\pp2\lab4\sample.json", "r") as info: 
    info = json.load(info) 
 
    for i in info["imdata"]: 
        print(i["l1PhysIf"]["attributes"]["dn"], "\t\t\t\t", i["l1PhysIf"]["attributes"]["speed"], " ", i["l1PhysIf"]["attributes"]["mtu"])