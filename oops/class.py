class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def sayCarDetails(self):
        print("Brand of Car is: ", self.brand)    
        print("Model of Car is: ", self.model)   
        return f"{self.brand} {self.model}" 
    

my_car = Car("Toyota", "Corolla")   
print(my_car.brand) 
print(my_car.model) 
print(my_car.sayCarDetails())

my_new_car = Car("TATA", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.sayCarDetails())
# in python __init__ is constructor and self is important for 
# for differeciete betwwen class members and parameters it similar to js this

