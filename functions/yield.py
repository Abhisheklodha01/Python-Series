# Generator function with yield

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        print(i)

even_generator(10) # it prints number 2, 4, 6, 8, 10 basically  
                   # third paramter 2 denotes skip number 2 means 1 beacuse it is exclusive       

# def even_generator2(limit):
#     for i in range(2, limit + 1, 2):
#         return i                 #problem
    
# for num in even_generator2(10) :
#     print(num)   


def even_generator2(limit):
    for i in range(2, limit + 1, 2):
        yield i                 
    
for num in even_generator2(10) :
    print(num)   

# Recursive function

def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)     

print(calculate_factorial(5))