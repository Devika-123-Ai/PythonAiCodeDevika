file=open('sample.txt','w')
file.write('hi how are you')
file.close()
#print("Hi im devika")

with open ("sample1.txt","w") as file:  #by using with automatically closes the file when the with block ends.
    file.write("what are you doing")
    

with open("sample1.txt","r") as file:  #you did not assign the opened file to file.if we dont write as file
    data=file.read()
    print(data)

with open("sample1.txt","a") as file:
    file.write("\n nothing much")
    
with open("sample1.txt") as file:
    print(next(file))
    print(next(file))

