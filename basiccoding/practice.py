def multiplication(a,b):
    return a*b
operation=multiplication
print(operation(5,10))



def subtraction(a,b):
    return a-b
def calculate(func,a,b):#Because calculate() takes another function through the parameter func
    return func(a,b)
print(calculate(subtraction,5,10))#calling the calculate() function and passing the subtraction() function as an argument along with the values 5 and 10.



def subtraction(a, b):
    return a - b
def calculate(subtraction, a, b):
    return subtraction(a, b)
print(calculate(subtraction, 5, 10))


def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def calculate(func, a, b):
    return func(a, b)

print(calculate(addition, 5, 10))
print(calculate(multiplication, 5, 10))





def add(a, b):
    return a + b
def caluculate(a, b):       
    result = add(a, b)
    #return result
    print("The result is:", result) 
caluculate(5, 10)


def calculate(func, a, b):
    return func(a, b)

print(calculate(lambda x, y: x + y, 10, 20))