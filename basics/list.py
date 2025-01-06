tea_varities = ["Black", "Green", "Oolong", "White"]
# print(tea_varities)

#slicing 
print(tea_varities[0:2]) # 0 -> start index, 2 ---> end index

tea_varities[3] = "Herbal"
# print(tea_varities)

# tea_varities[1:2] = "Lemon" # changing value, not prefered way it insert value like that 'L', 'e'

tea_varities = ["Black", "Green", "Oolong", "White"]
tea_varities[1:2] = ["Lemon"] # insert at 1
tea_varities[1:3] = ["Green", "Masala"] # insert at 1, 2
# print(tea_varities) 

print(tea_varities[1:1]) # return an empty array 

tea_varities[1:1] = ["test", "test"] #it insert these values into list 
                                     #beacuse our start and end index is same  

tea_varities[1:3] = [] # delete using insert method 


tea_varities = ["Black", "Green", "Oolong", "White"]

# for loop on list 
for tea_variety in tea_varities:
    if tea_variety == "Black":
        print(1)
    elif tea_variety == "Green":
        print(1)
    else:
        print(3)   


# append method 
tea_varities.append("Masala")
if "Masala" in tea_varities:
    print("I have Masala Tea")

#pop method 
tea_varities.pop()
print(tea_varities) 

#remove method  
tea_varities.remove("Oolong")

#insert method
tea_varities.insert(1, "Oolong")

tea_varities_copy = tea_varities # in this both points to the same memory location 
tea_varities_copy = tea_varities.copy() # in that new copy is created 
print(tea_varities_copy)

squared_nums = [x ** 2 for x in range(10)] # it strore squares from 1 to 10 in list
print(squared_nums)
cube_nums = [x ** 3 for x in range(10)]
print(cube_nums)