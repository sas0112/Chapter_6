import random

# store information about a pizza being ordered.
pizza = {
    "crust": ["thick","thin","medium"],
    "size": [6,8,12],
    "topping": ["mushrooms","extra cheeze","chicken"],
}

# summarize the order.
print("you ordered a " + pizza["crust"][random.randint(0,2)] + '-crust pizza' +
      ' with the following toppings and size:')
print("\t" + pizza["topping"][random.randint(0,2)].title())
print("\t" + str(pizza["size"][random.randint(0,2)]))