# import math 
# print(math.sqrt(16))
# print(math.pow(2,4)) #2*2*2*2
# print(math.pi)

# random
import random
# print(random.random())
# print(random.randint(999,10000))
# print(random.choice(["apple","banana","orange","watermelon"]))


# date and time
# import datetime
# # today = datetime.date.today()
# today = datetime.datetime.now()
# print(today)


# # os
# import os
# print(os.name)
# print(os.getcwd())
# os.mkdir("newfolder")


# re - regular expression

import re
# text = "this is my number 7894561237"

# num = r'\d{10}'

# match = re.search(num,text)
# if match:
#     print("match Found:",match.group())


# password = input("Enter your Password:")

# pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&]).{8,}$'
# if re.match(pattern,password):
#     print("Strong Password")
# else:
#     print("Password is weak")


# statistics
# import statistics
# value = [10,20,30,40,45]
# print(statistics.median(value))
# print(statistics.mean(value))


# collection counter

from collections import Counter
nums = [100,100,100,110,110,110,110,110,111,111,112,112,113,113]
print(Counter(nums))