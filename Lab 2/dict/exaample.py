#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

x = thisdict.items()

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.popitem()
print(thisdict)

#The pop() method removes the item with the specified key name:


thisdict.pop("model")
print(thisdict)

#The clear() method empties the dictionary:

thisdict.clear()
print(thisdict)

#You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)
  