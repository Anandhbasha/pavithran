try:
    num = int(input("Enter the Number:"))
    a=20
    print(a/num)
except(ZeroDivisionError,ValueError):
    print("Enter value must be postive number only numbers")
finally:
    print("Completed succesfully")

a =60
print(a)

# FileNotFoundError
# KeyError
# TypeError