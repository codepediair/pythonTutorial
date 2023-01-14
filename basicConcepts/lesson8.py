# List
myList = [2,1,4,7,5, 2.1, 'hello',14]

# print(myList[0] + myList[3])

# print(len(myList))
# print(myList[len(myList)])

myList.remove('hello')
myList.pop(2)


myList.append(105)
myList.insert(3, 107)

myList.sort()

for i in range(len(myList)):
    if (myList[i] % 2 == 0):
        print(myList[i], end = ' ')
print()
sco = []
tmp = 0
for i in range(20):
    tmp = int(input("please enter a number : "))
    sco.append(tmp)

print(sco)

for i in range(len(sco)):
    if (sco[i] > 5):
        print(sco[i])