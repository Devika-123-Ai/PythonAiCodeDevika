#Create a PhonePayWallet with private balance and add_money() and pay() methods.

class PhonePayWallet:
    def __init__(self,initialdeposit):
          self.__balance=initialdeposit

    def add_money(self,money):
          self.__balance = self.__balance + money
          return self.__balance
    def pay(self,money):
        self.__balance = self.__balance - money          
        return self.__balance

class Test:
    myacc = PhonePayWallet(1000)
    addmoney=myacc.add_money(500)
    print("after adding money to wallet" ,addmoney )

    paidmoney=myacc.pay(200)
    print("after paying money from wallet" ,paidmoney)