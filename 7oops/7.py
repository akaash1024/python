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

    @staticmethod    
    def generalDetails():
        return "cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def fuelType (self):
        return "Electric Charge"


safari = Car("tata", "safari")
print(safari.generalDetails()) #//this allow to call this method, but we dont want that
print(Car.generalDetails()) #after adding line.19 @static and removing self it works 







