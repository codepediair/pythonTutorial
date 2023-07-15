class vehicle:
    def __init__(self,brand,model,color,year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def age(self):
        return 2023 - self.year


class Car(vehicle):
    def __init__(self,brand,model,color,year,kind):
        super().__init__(brand,model,color,year)
        self.kind = kind
    
    def __str__(self):
        return self.brand + " " + self.model

obj1 = Car('ford','mustang', 'black', 1969,'rodester')
# obj2 = Car('bmw','x6', 'red', 2020)
# obj3 = Car('pekan','javanan', 'tomato')
# obj2 = Car()

# print(obj1.brand)
# print(obj1.age())
 
print(obj1.age())
# print(obj2)
# print(obj2.brand)
# print(obj3.brand)