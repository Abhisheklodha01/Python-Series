# Print the multiplication table up to 10 and skip 5 

number = 3

for i in range(1, 11):
    if i == 5:
      continue

    print(number * i)