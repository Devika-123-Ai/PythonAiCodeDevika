#Storing the function in a variable

def greet():
    print('HI')
welcome = greet()       #greet() is not returning any value so O/P:none
print(welcome)

def greet():
    return 'Hello'
welcome = greet()       #greet() is returning a value so O/P:Hello
print(welcome)

def greet():
    print('Hello')      
welcome = greet         #stores function itself as a value in a variable so o/p:function object
print(welcome)  

def add(a, b):
    return a + b    
operation=add   
print("The sum is:", operation(5, 10))   
#storing the function in a variable is useful when we want to pass the function as an argument to another function or when we want to return a function from another function.
 

 #higher order function is a function that takes another function as an argument or returns a function as a result.

#takes a function as an argument
def add(a, b):
    return a + b

def operation(func, a, b):
    return func(a, b)

print("The sum is:", operation(add, 5, 10))


def add(a, b):
    return a + b

def calculate(func, x, y):
    return func(x, y)

print(calculate(add, 5, 10))     #above 2 examples for taking a function as an argument.

# returning a function as a result
def operation():
    def add(a, b):
        return a + b

    return add

result = operation()

print(result(5, 10))