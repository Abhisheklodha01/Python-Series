class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def sayCarDetails(self):    
        print("Model of Car is: ", self.__model)   
        return f"{self.__brand} {self.__model}" 
    
    def get_brand(self):
        return self.__brand
    
    def set_model(self, model):
        self.__model = model

my_car = Car("Toyota", "Corolla")   
# print(my_car.__brand) # error
print(my_car.get_brand()) 
my_car.set_model("Tata")
print(my_car.sayCarDetails())


# for making private we use __varible_name by default it is public