# f = open("test.txt", 'w')
a = open("new.txt", 'x')
f = open("test.txt", 'a')
f.write("i like python")
f.close()



f = open("test.txt", 'r')
print(f.read())
# print(f.readline())
# print(f.readline())
f.close()


