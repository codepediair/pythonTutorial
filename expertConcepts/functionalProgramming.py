from numpy import random
# print("hello world")
# f(x) = x^2

# def msg(x):
#     print(x)

# msg('hello functions')
# msg('this is python')

# def add(x, y):
#     return x + y

# def findMin(x, y):
#     if (x < y):
#         return x
#     else:
#         return y

# print(add(2, 4) + findMin(8, 12))

# isPrime = True
# n = int(input())

# for i in range(2,n):
#     if (n % i == 0):
#         isPrime = False
#         break

# if (isPrime):
#     print("prime")
# else :
#     print("not prime")


def isPrime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

# print(isPrime(17))
# print(isPrime(15))

# for i in range(1000,10000):
#     if(isPrime(i)):
#         print(i)
#         break

# 0 1 1 2 3 5 8 ...

def fibo(n):
    a, b, c, i = 0, 1, 0, 2
    if (n == 1):
        return a
    elif (n == 2):
        return b
    elif (n > 2):
        while(i < n):
            c = a + b
            a = b
            b = c
            i += 1
        
    return c

if __name__ == "__main__":
    cnt = 0
    i = 4
    while (cnt < 12):
        if(isPrime(fibo(i))):
            print(i,fibo(i))
            cnt += 1
        i += 1
