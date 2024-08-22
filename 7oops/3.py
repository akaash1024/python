class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.model} {self.brand}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

myTesla = ElectricCar("Tesla", "Model S", "50kWh")
print(myTesla.brand)
print(myTesla.fullName())


