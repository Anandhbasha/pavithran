class Dad:
    def house(self):
        print("Own House")
class Son(Dad):
    def bike(self):
        print("Own Bike")

s = Son()
s.house()
s.bike()