# find first Non-Repeated Character

input_str = "aaaaabdbcbb"

for char in input_str: 
    if input_str.count(char) == 1:
        print("Character is :", char)
        break