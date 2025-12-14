class Calc:
    def add(self,a=0,b=0,c=0):
        return a+b+c
    
cal = Calc()
print(cal.add(10,20,30))
print(cal.add(10,20))
print(cal.add(10))