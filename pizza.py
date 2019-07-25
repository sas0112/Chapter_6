# store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "topping": ["mushrooms","extra cheeze"]
}
# summarize the order.
print("you ordered a " + pizza["crust"] + '-crust pizza' +
      'with the following toppings:')

for topping in pizza["topping"]:
    print(topping)