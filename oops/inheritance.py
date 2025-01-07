class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def sayCarDetails(self):
        print("Brand of Car is: ", self.brand)    
        print("Model of Car is: ", self.model)   
        return f"{self.brand} {self.model}" 
    
class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size


tesla_car = ElectricCar("Tesla", "Tesla S", "85kWh")
print(tesla_car.sayCarDetails())
