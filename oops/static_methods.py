class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def sayCarDetails(self):
        print("Brand of Car is: ", self.brand)    
        print("Model of Car is: ", self.model)   
        return f"{self.brand} {self.model}" 
    
    @staticmethod
    def general_description():
        return "Cars are mode of transport"


my_car = Car("Toyota", "Corolla")   
print(my_car.general_description())
print(Car.general_description())



