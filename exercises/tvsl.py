import sys

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# myList[0] = 15
# myTuple[0] = 15

print(sys.getsizeof(myTuple))
print(sys.getsizeof(myList))
