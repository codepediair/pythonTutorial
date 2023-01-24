# print("hello world")
# f(x) = x^2

# def msg(x):
#     print(x)

# msg('hello functions')
# msg('this is python')

def add(x, y):
    return x + y

def findMin(x, y):
    if (x < y):
        return x
    else:
        return y

print(add(2, 4) + findMin(8, 12))