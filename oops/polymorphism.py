class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def sayCarDetails(self):       
        return f"{self.__brand} {self.__model}" 
    
    def get_brand(self):
        return self.__brand
    
    def set_model(self, model):
        self.__model = model

    def fuel_type(self):
        return "Petrol or Diesel"    
    

class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size    

    def fuel_type(self):
        return "Electric charge"        

tesla_car = ElectricCar("Tesla", "Tesla S", "85kWh")
print(tesla_car.fuel_type())

my_car = Car("Toyota", "Corolla")   
print(my_car.fuel_type())