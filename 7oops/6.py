class Car:
    totalCar=0

    def __init__(self,brand,model):
        self.__brand = brand #putting __ make is private
        self.model = model
        # self.totalCar+=1 OR
        Car.totalCar+=1

    def getBrand (self):
        return self.__brand + "!"
    
    def fullName(self):
        return f"{self.model} {self.__brand}"
    
    def fuelType (self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def fuelType (self):
        return "Electric Charge"

# myTesla = ElectricCar("Tesla", "Model S", "50kWh")
# safari = Car("tata", "safari")
# safariThree = Car("test","test")
# # print(safariThree.totalCar) /this is not right way to access instead 
# print(Car.totalCar)


# define like, this is also works
# ElectricCar("Tesla", "Model S", "50kWh") #1
Car("tata", "safari")                    #2
Car("test","test")                       #3          
print(Car.totalCar)


