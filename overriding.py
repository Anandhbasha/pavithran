class Res:
    def order(self):
        print("Order from Res")
class Vres(Res):
    def order(self):
        print("Order from VegRes")
class NVres(Res):
    def order(self):
        print("Order from Non-Veg-Res")
    
R = Res()
R.order()
Vr = Vres()
Vr.order()
Nvr = NVres()
Nvr.order()