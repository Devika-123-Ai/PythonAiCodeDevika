#Create a BankAccount with private balance and deposit() / withdraw() methods.

class BankAccount():
    def __init__(self,initialdeposit):
        self.__balance = initialdeposit
    #this methods input is money,output is balance,logic is it adds money to initialdeposit.
    def deposit(self,money):
        self.__balance = self.__balance + money 
        return self.__balance
    #logic it deletes the money from current balance 
    def withdraw(self,money):
        self.__balance = self.__balance - money 
        return self.__balance

class Test():
    myaccout = BankAccount(2000)# we are not using self._balance directly because its private so we just initializing though constructor
    deposit= myaccout.deposit(1000)
    print("after deposit current bal",deposit)
    withdrawl= myaccout.withdraw(500)
    print("after withdrawls current bal" ,withdrawl)

    
