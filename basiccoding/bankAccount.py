#Create a BankAccount with private balance and deposit() / withdraw() methods.
ifsccode=12345678
class BankAccount():
    def __init__(self,initialdeposit,pinno):
        self.__balance = initialdeposit
        self.__pinno = pinno
        print("inital deposit",self.__balance )
        print("pin no" , self.__pinno)
    def deposit(self,money):
        self.__balance = self.__balance + money 
        return self.__balance
    
    def withdraw(self,money):
        self.__balance = self.__balance - money 
        return self.__balance

class Test():
    myaccout = BankAccount(2000,1234)# we are not using self._balance directly because its private so we just initializing though constructor
    
    deposit= myaccout.deposit(1000)
    print("after deposit current bal",deposit)
    withdrawl= myaccout.withdraw(500)
    print("after withdrawls current bal" ,withdrawl)

    print(ifsccode)

    
