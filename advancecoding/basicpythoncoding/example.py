
list1 = [1, 2, 3, 4, 5]
def sample(list1):
    for i in list1:
        if i == 4:
            print("zero")
            break
    else:
        print("non-zero")
    # return i

sample(list1)