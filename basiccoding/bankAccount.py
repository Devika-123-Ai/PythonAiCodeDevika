#Create a BankAccount with private balance and deposit() / withdraw() methods.
transaction_limit = 10000    # Global variable 
class BankAccount():
    bankname = 'citybank'
    total_accounts =0 
    # ifsccode=686878   # class variables
    
    def __init__(self,accountno,customername,initialdeposit,pin):
        self.__accountno = accountno
        self.__customername = customername
        self.__balance = initialdeposit
        self.__pin = pin                  #instance variables 
        
        # print("inital deposit",self.__balance)

        BankAccount.total_accounts += 1
        
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
    
    def display(self):
        return {
            "accountno":self.__accountno,
            "customername":self.__customername,"initialbalance": self.__balance,"pin":self.__pin}
    
    def withdraw(self, amount):

       if amount > transaction_limit:
        print("Transaction limit over")

       elif amount > self.__balance:
        print("Insufficient balance")

       else:
        print("Sufficient balance")
        self.__balance = self.__balance - amount
        return self.__balance
    
    # @classmethod
    # def total_accounts(cls):
    #     return cls.total_accounts

    
class Test():

    myaccout = BankAccount(987654321,"devika",1000,1234)
    myaccout = BankAccount(123445667,"pandu",1000,4321)# we are not using self._balance directly because its private so we just initializing though constructor
    
    deposit= myaccout.deposit(2000)
    print("after deposit current bal",deposit)

    withdrawl= myaccout.withdraw(11000)
    print("after withdrawls current bal" ,withdrawl)

    print(myaccout.display())

    totalaccounts = BankAccount.total_accounts
    print(totalaccounts)

    

    
