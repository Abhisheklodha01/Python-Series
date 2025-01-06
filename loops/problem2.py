# Calculate sum of even number 
input_number = input("Enter Number \n") 
number = int(input_number)
sum_even = 0

for i in range(1, number+1):
    if i % 2 == 0:
        sum_even += i

print(sum_even)        