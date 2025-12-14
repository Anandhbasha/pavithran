class Bank:
    def loan(self):
        print("Bank loan")
class Eduction(Bank):
    def edu(self):
        print("This education Loan")
class home(Bank):
    def homes(self):
        print("This home Loan")

e=Eduction()
h=home()

e.loan()
h.loan()
