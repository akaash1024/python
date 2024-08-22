class Car:
    totalCar=0

    def __init__(self,brand,model):
        self.__brand = brand #putting __ make is private
        self.__model = model
        # self.totalCar+=1 OR
        Car.totalCar+=1

    def getBrand (self):
        return self.__brand + "!"
    
    def fullName(self):
        return f"{self.__model} {self.__brand}"
    
    def fuelType (self):
        return "Petrol or Diesel"

    @staticmethod    
    def generalDetails():
        return "cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def fuelType (self):
        return "Electric Charge"

myTesla = ElectricCar("Tesla", "Model S", "50kWh")
safari = Car("tata", "safari")

print(isinstance(myTesla,Car))
print(isinstance(myTesla,ElectricCar))






