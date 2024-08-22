class Car:
    def __init__(self,brand,model):
        self.__brand = brand #putting __ make is private
        self.model = model

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

myTesla = ElectricCar("Tesla", "Model S", "50kWh")
# print(myTesla.__brand) //throwing error
# print(myTesla.brand) //throwing error its private now
print(myTesla.getBrand())
print(myTesla.fuelType())

safari = Car("tata", "safari")
print(safari.fuelType())
