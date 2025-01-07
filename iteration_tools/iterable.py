myList = [1,2,3,4]
I = iter(myList)
print(I)
print(I.__next__())

f = open('chai.py')
print(iter(f) is f)

# read about iterations more from notes 

# iterable things: list, dict, file, range()

# __next__ and next() both are same 

