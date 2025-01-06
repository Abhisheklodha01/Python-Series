tea_types = ("Black", "Green", "Oolong")
print(tea_types)

#slice 
tea_types[0:2]

# tea_types[0] = "Lemon" # error beacuse tuple is immutable 

more_tea = ("Herbale", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have Green Tea")

more_tea.count("Herbal")

(black, green, oolong) = tea_types # it is similar to destructoring objects
print(black)

print(type(tea_types))
#nesting is possible in tuples 