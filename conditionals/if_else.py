# challange One --> Age Categorization
input_age = input("Enter Your Age \n")
age = int(input_age)

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")    
elif age < 60:
    print("Adult")    
else:
    print("Senior")    