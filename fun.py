# def greet():
#     print("Welcome")

# greet()

# def add(a,b):
#     print(a+b)

# add(50,60)
# add(80,70)
# add(68,75)
# add(82,71)
# add(66,60)
# add(89,97)

# return
# def add(a,b):
#     return a+b

# print(add(89,97))


# default

def values(Schoolname="SRVS"):
    print("schoolName is:",Schoolname)

# values()

# # keyword Argument
# def students(name,age):
#     print(name,age)

# students(age=22,name="Arun")



# Variable length Arguments *args **kwargs
# def total(*a):
#     print(sum(a))

# total(70,80,90)

# def profile(**data):
#     print(data)


# profile(name="Ajay",age=22)


# def calc(a,b):
#     return a+b,a-b,a*b

# a,s,m = calc(10,5)
# print(a,s,m)


# # lambda function
# square = lambda b:b*b
# print(square(5))

# scope of the variable

# x=10 #global scope
# def calls():
#     y=20 #function scope or local scope
#     print(x)
# calls()
# print(y)


def login(user,pwd):
    if user=="admin" and pwd=="123":
        return "Login Successfull"
    else:
        return "Invalid Credentials"
    
print(login("admi","123"))