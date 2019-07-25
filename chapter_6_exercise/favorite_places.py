favorite_places = {
    "alice":["boston","washington","beijing"],
    "ben":["seattle","berkeley","new york"],
    "wang":["nairobi","cairo","shanghai"],
}

for key,values in favorite_places.items():
    print("These are the favorite places for: " + key.title())
    for value in values:
        print(value.title())
    print("\n")