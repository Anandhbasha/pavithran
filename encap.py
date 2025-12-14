class ATM:    
    def __init__(self):
     self.__balance = 1000 #private
    def deposit(self,amount):
       self.__balance+=amount
    def showBalance(self):
       return self.__balance

atm = ATM()
print(atm.showBalance())
atm.deposit(10000)
print(atm.showBalance())