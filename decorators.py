# def create_add(x):
#     def add(y):
#         return x + y
    
#     return add

# add_2 = create_add(2)
# print(add_2(10))

def hello_decorators(func):
    def inner1(*args,**kwargs):
        print("step one")

        res = func(*args,**kwargs)

        print("finall step")
        return res
    return inner1

@hello_decorators
def add(a,b):
    print("we are in add function")
    return a + b

@hello_decorators
def mul(a,b):
    print("we are in multiple")
    return a * b


print(add(7,6))
print(mul(2,9))

