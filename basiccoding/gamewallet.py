#Create a GameWallet where players can add and spend game coins.

class GameWallet():
    def __init__(self,coins):
        self.__coins = coins
    def add_coins(self,coins):
        self.__coins = self.__coins + coins
        return self.__coins
    def spend_coins(self,coins):
        self.__coins = self.__coins - coins
        return self.__coins

class Test():
    wallet = GameWallet(5000)
    print("initial coins",wallet)

    addcoins= wallet.add_coins(500)
    print("added coins now total coins", addcoins)

    spendcoins= wallet.spend_coins(1000)
    print("spent coins now remaining coins", spendcoins)


        