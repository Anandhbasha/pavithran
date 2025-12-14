# dad,mom->son

class Dad:
    def prints(self):
        print("He is my dad")
class mom:
    def parent(self):
        print("He is my mom")
class son(Dad,mom):
    pass

s=son()
s.parent()
s.prints()