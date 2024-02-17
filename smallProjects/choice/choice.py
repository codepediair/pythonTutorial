import random

foods = ['gormesabzi', 'gemeh', 'kabab', 'koko', 'adaspolo', 'lobiapolo', 'fesenjan']

for i in range(7):
    _choice = random.choice(foods)
    foods.remove(_choice)
    print(_choice)

