chai = "Masala Chai"
first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]

chai2 = "Lemon Chai "
print(chai2.replace("Lemon", "Ginger"))

chai = "Lemon Ginger Masala Mint"
print(chai.split(" ")) # return a list 

print(chai.find("Chai")) # return an index of starting
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai "

print(order.format(quantity, chai_type)) # inject variable 

# list to string 
chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))
print(", ".join(chai_variety))

# get length of chai
chai = "Masala chai"
print(len(chai))

# for loop
for letter in chai:
    print(letter) 


chai = "He said, \"Masala chai is awesome\" "
print(chai)

# unicode = "c:\\user\\pwd"
# unicode = r"c:\user\pwd"

chai = "Masala chai"
print("Masala" in chai) # asking question to python