#Create a CreditCard class with private credit limit and controlled spending

class Creditcard():
    def __init__(self,creditlimit):
        
        self.__creditlimit=creditlimit

        #controlling spend based on creditlimit 

    def spend(self,spendingamount):
        if(spendingamount<=self.__creditlimit):
            self.__creditlimit = self.__creditlimit-spendingamount
            print("success")
        else:
            print("it reaches max limit")
        return self.__creditlimit
class Test:
    creditcardlimit = Creditcard(10000)
    print("creditcard limit",creditcardlimit)
    
    spentamount = creditcardlimit.spend(11000)
    print(spentamount)