class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def sayCarDetails(self):
        print("Brand of Car is: ", self.brand)    
        print("Model of Car is: ", self.model)   
        return f"{self.brand} {self.model}" 
    

class Battry:
    def battry_info(self):
        return "This is battry" 
    
    
class Engine:
     def engine_info(self):
        return "This is engine" 
    
class ElectricCar(Battry, Engine, Car):
    pass


my_tesla = ElectricCar("Tesla", "Tesla S")
print(my_tesla.engine_info())
print(my_tesla.battry_info())