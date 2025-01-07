username = "abhisheklodha01" # globally accessible

# function test() {
#    in other languages
# }

# in python scope space is eveluated on the basis of indentation 

def greet():
    username = "Abhishek Lodha"
    print(username)


greet()    
print(username)

x = 87
def func():
    global x # gives global reference x is not redefined  
    x = 88

func()
print(x)    

# closure is also present in python which is completly similar to js 

def func2(): 
    x = 10
    def innerFunc():
        return x ** 2
    return innerFunc

result = func2()
print(result())

def func3(num): 
    x = 10
    def innerFunc():
        return x ** num
    return innerFunc

result = func3(2)
result2 = func3(3)
print(result)
print(result2)
print(result())
print(result2())