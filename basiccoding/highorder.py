from unicodedata import name


def hello(name):
    print("Hello "+name)
    def greet():
        print("Good Morning "+name)
    def welcome():
        print("Welcome "+name)

    if name=="devika": 
        return greet
    else: 
        return welcome
func =hello("devikaji")
func()