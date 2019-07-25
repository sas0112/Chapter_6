favorite_numbers = {
    "alice":[1,2,3],
    "ben":[4,5,6],
    "wang":[7,8,9],
}

for key,values in favorite_numbers.items():
    print("These are the favorite numbers for: " + key.title())
    for value in values:
        print(str(value))
    print("\n")