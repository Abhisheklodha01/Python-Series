# problem: write a function that find square 

def find_squares(number):
    return number*number

square_value = find_squares(9)
print(square_value)

def addToNumbers(num1, num2):
    return num1 + num2

addition_result = addToNumbers(10, 20)
print(addition_result)

# default value

def greet(name = "User"):
    return "Hello" + name + "!"