x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)    #assign values to multiple variables

x = y = z = "Orange"
print(x)
print(y)
print(z)    #one value to multiple variables(VWhat is a correct syntax to add the value 'Hello World', to 3 variables in one statement?)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)    #unpacking list

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)          #output multiple variables separated by ,

fruits = {"apple", "banana"}

# Using discard() -> Safe
fruits.discard("orange")  # No error, set remains {"apple", "banana"}

# Using remove() -> Error
fruits.remove("orange")   # KeyError: 'orange'