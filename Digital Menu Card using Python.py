class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ' : ' + str(self.price)
   
def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu

import random
import time

names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Momos', 'Donut', 'sambar']

costs = [250, 150, 300, 240, 65, 55, 120, 150]

offer=["You got an icecream worth 80Rs for free","Get flat 20% off on SBI credit cards","Flat 30% off on minimum bill of 500Rs","Get Pizza and Burger at only 400 Rs","You won a coupon of 100Rs","You got a compliment softdrink"]
x=time.strftime("%a")
if x=="Mon":
    names.append("Manchuria")
    costs.append(200)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
elif x=="Tue":
    names.append("Garlic Bread")
    costs.append(250)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
elif x=="Wed":
    names.append("Brownie")
    costs.append(100)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
elif x=="Thu":
    names.append("Spaghetti")
    costs.append(280)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
elif x=="Fri":
    names.append("Mojito")
    costs.append(150)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
elif x=="Sat":
    names.append("Peri Peri Fries")
    costs.append(100)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
elif x=="Sun":
    names.append("Moburg")
    costs.append(120)
    Foods = buildmenu(names, costs)
    n = 1
    print("Menu:")
    for el in Foods:
        print(n,'. ', el)
        n = n + 1
    print("todays special dish is",names[8])
    print(random.choice(offer))
    names.pop(8)
    costs.pop(8)
