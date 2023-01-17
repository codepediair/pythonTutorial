# List
myList = [2,1,4,7,5, 2.1, 'hello',14]

# print(myList[0] + myList[3])

# print(len(myList))
# print(myList[len(myList)])

# myList.remove('hello')
# myList.pop(2)


# myList.append(105)
# myList.insert(3, 107)

# myList.sort()

# for i in range(len(myList)):
#     if (myList[i] % 2 == 0):
#         print(myList[i], end = ' ')
# print()
# sco = []
# tmp = 0
# for i in range(20):
#     tmp = int(input("please enter a number : "))
#     sco.append(tmp)

# print(sco)

# for i in range(len(sco)):
#     if (sco[i] > 5):
#         print(sco[i])

# tuple
myTuple = (1, 2, 3, 4, 5, 6)
# print(len(myTuple))
for i in range(len(myTuple)):
    print(myTuple[i])

myList[0] = 105
# myTuple[0] = 100

tmp = []
tmp = list(myTuple)
tmp[0] = 105
myTuple = tuple(tmp)
del tmp
print(myTuple)


# set
mySet = {1, 3, 4, 5, 6}

# dictionary
mydict = {
    "name":"mahdi",
    "favLang":["python","c","cpp"],
    "age":30
}

mydict['favColor'] = 'black'
mydict.pop('age')
print(mydict)

for i in mydict.keys():
    print(i)

