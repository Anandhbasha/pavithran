# # # # print("Hello Welcome",end="")
# # # # print("This is my first python code")
# # # # a=10
# # # # print(a)
# # # print("apple","banana","kiwi",sep="-")


# # # a=10 # = assignment operator
# # # a=20
# # # print(a)

# # # datatypes
# # # simple data types
# # # int
# # # a=20
# # # print(type(a))
# # # # float
# # # a=10.0
# # # print(type(a))
# # # string
# # # a="vijay"
# # # print(type(a))
# # # # boolean
# # # a=True
# # # print(type(a))

# # # complex data types
# # # list
# # ''' list = [20,10.0,"vijay",True] #index 0 1 2 3
# # print(list)
# # print(list[0])
# # print(list[1]) '''

# # # list = [20,10.0,"vijay",True]
# # # list[0] = 50
# # # print(list)
# # # tuple
# # # tuple = (10,20,30,40,50)
# # # tuple[0] = 80
# # # print(tuple[0])
# # # print(tuple[2])
# # # set
# # # sets = {101,105,106,102,104,103,101,102,103}
# # # # print(sets[0])
# # # # print(sets)
# # # # dictionary
# # # person = {
# # #     "name":"arun",
# # #     "age":22
# # # }
# # # # print(person)
# # # print(person['name'])

# # # arithmetic Operator
# # print(10+5) #addtion
# # print(10-5) #substraction
# # print(5*2) #Multiplication
# # print(10/2) #Division
# # print(10//2) # Floor Division
# # print(10%3) #Modulus
# # print(2**3) #2*2*2 Exponentiation

# # # Comparision
# # a=10
# # b=10
# # # print(a==b) #is Equal
# # # print(a!=b) #not equal
# # # print(a>b) 
# # # print(a<b) 
# # print(a<=b) 
# # print(a>=b) 

# # logical Operator
# # and or Not

# # age = 20
# # State = "HR"
# # print(age>=18 and State=="TN")
# # print(age>=18 or State=="TN")
# # print(not age>18)

# # assignment operator
# # =
# # a=5
# # b=10

# # # a=a+b
# # a+=b
# # print(a)

# # Membership 
# # in
# # not in

# # list1 = ["apple","banana","papaya","grapes"]
# # print("apple" not in list1)

# name = "AJay"
# print("J" in name)

# # idendity 
# a=[1,2,3,4]
# b=a
# c=[1,2,3,4]

# print(a is b)
# print(c is not a)

# Json
person = {
    "name":"arun",
    "age":22
}

print(type(person))

import json
newData = json.dumps(person)
print(type(newData))
print(newData)
print(person)

returnValue  = json.loads(newData)
print(type(returnValue))