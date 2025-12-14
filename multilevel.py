# Grandpa->Dad->Son
class grandPa:
    def gender(self,gen):
        self.gen = gen
        print("the gender is :",self.gen)
class dad(grandPa):
    def genders(self):
        print("He is my dad")
class son(dad):
    pass

s =son()
s.genders()
s.gender("Male")
