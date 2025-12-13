# carModel = "i10"
# carMilage = 17
# noofWheels = 4
# noofSheets = 5
# noofAirgbags=6

# def acc():
#     print("Car moves")
# def brake():
#     print("Car stops")


class Car:
    carModel = "i10"
    carMilage = 17
    noofWheels = 4
    noofSheets = 5
    noofAirgbags=6
    # methods
    def acc(self):
        print(self.carModel,"moves")
    def brake(self):
        print(self.carModel,"stops")

car1 = Car() #instence creating
car1.carModel = "i20"
car1.acc()

car2 = Car()
car1.carModel = "venue"
car2.acc()