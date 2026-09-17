def add(a, b):
    return a + b
addition=add                #a higher order function is a function that takes another function as an argument or returns a function as a result
print(addition(10,20))

def loud(name):
    print("hhhhh")
    return name.upper()
def quiet(name):
    return name.lower()



def greet():
    return loud("name1")


res=greet(loud)   #greet is a higher order function because it takes another function as an argument  
print(res)

# def greet():
#     print("Hello")
# def call(func):
#     print("hi")
#     func()
# call(greet)   #call is a higher order function because it takes another function as