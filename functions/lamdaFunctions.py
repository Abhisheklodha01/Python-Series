# lamda function : function without name
# find cube of a number
cube = lambda x:x ** 3
print(cube(3))

# function with args that can take any number of arguments 

def sum_all(*args):
    return sum(args)

print(sum_all(2, 3))
print(sum_all(2, 3, 4))
print(sum_all(2, 3, 4, 5))
print(sum_all(2, 3, 6, 7, 8))

# *args: denotes multiple arguments
# implementatio take array input from user then iterate over array and take values than calculate 

def sum_imp(*args):
    sum = 0
    for i in args:
        sum += i
    return sum    


# Problem: Create a function that accepts any number of keyword arguments and prints them 
# in the format key:value 

# print_kwargs(name = "shaktiman", power = "lazer") arguments

def print_kwargs(name, power): 
    print("Name", name, "Power", power)

print_kwargs(power="lazer", name="shaktiman") #jab hum named parameter dete hai to order matter nhi karta    

def print_kwargs(**kwargs): 
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackaal")