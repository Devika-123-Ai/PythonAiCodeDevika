
#function is calling another function
def add(a, b):
    return a + b

def caluculate(a, b):       #a,b in add() local variable so scope ends after the function call
    result = add(a, b)
    # return result
    print("The result is:", result) 
caluculate(5, 10)
#function is calling another function
#function can be passed as an argument/passing the function itself as a value this concept is called first class function.
#function that takes another function as an argument is called higher order function

