#Dictionary in Python
chai_types = {
    "Masala" : "Spicy",
    "Ginger" : "Zesty",
    "Green" : "Mild"
}

# one way to iterate over dict.
for chai in chai_types:
    print(chai, chai_types[chai])


# second way to iterate over dict.
for key, value in chai_types.items():
    print(value)


#print length of dict
print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"

#remove item form dict
chai_types.pop("Earl Grey")

# chai_types.popitem()
print(len(chai_types))

del chai_types["Green"]

#copy dict 
chai_types_copy = chai_types.copy()
print(chai_types_copy)

#Multi Dictionary
tea_shop = {
    "chai": {"Masala" : "Spicy", "Ginger" : "Zesty"},
    "Tea" : {"Green" : "Mild", "Black" : "Strong"}
}
# print(tea_shop)

# print(tea_shop["chai"]["Ginger"])

squared_nums = {x : x ** 2 for x in range(5)}
print(squared_nums)

squared_nums.clear()

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

new_dict = dict.fromkeys(keys, keys) # it sotres hole keys list for a single key 
print(new_dict)


