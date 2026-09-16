for i in range(1,10):
   if i%3==0:
       continue
print(i)

    #instead of writing more no of statements we can use looping.
print(list(range(10)))
print(range(5,10))
print(list(range(5,10)))
print(list(range(1,10,2)))# only odd no
print(list(range(2,10,2)))#even 
print(list(range(10,0,-1)))


#Before completing the sequence if we want to jump /stop we can use break
#terminate the loop in between then we need condition ---if
for i in range(1,10):
    if i==5:
        break
    print(i)
print("out of stock")

list1=["A","B","C"]
list2=['a','b','c']
#for i in list2:
list1.append(list2)
print(list1)

list1=["A","B","C"]
list2=['a','b','c']
list1.extend(list2)
print(list1)
