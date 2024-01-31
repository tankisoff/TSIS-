x = 200
print(isinstance(x, int))


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
bool("abc")
bool(123)

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")