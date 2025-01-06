# Challange 2: movie ticket pricing 

input_age = input("Enter Your Age \n")
age = int(input_age)
day = "Wednesday"
price = 12 if age >= 18 else 8
if day == 'Wednesday':
    price = price - 2
if age < 18:
    print("Ticket Price is: $", price)
else:
    print("Your Ticket Price is: $", price)    
  