# def func():
#     return          #o/p:None
# func()

# def cal(a,b):
#     return a+b          #o/p:30
# sum=cal(10,20)
# print(sum)

# def func():
#     i=10            # no o/p
# func()

# def cal(a,b):
#     print(a+b)      #we are not returning anything but o/p-30 because we printing

# cal(10,20)


# def cal(a,b):
#     return a+b  
# cal(11,12)
class Countdown:
    def __init__(self):
        self.n = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration

        print(self.n)
        self.n -= 1


c = Countdown()

next(c)
next(c)
next(c)
