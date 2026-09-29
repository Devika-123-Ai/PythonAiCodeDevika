#Create an AmazonWallet with private balance and purchase() method.

class AmazonWallet():
    def __init__(self,balance):
        self.__balance = balance
    def purchase(self,money):
        self.__balance = self.__balance - money
        return self.__balance

class Test():
    test = AmazonWallet(5000)

    remainingbalance = test.purchase(500)
    print("after purchasing remaining balance",remainingbalance)