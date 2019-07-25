curry = {
    "kind": "dog",
    "owner's_name": "andrew jackson",
}
betty = {
    "kind": "cat",
    "owner's_name": "ben ham",
}
kile = {
    "kind": "snake",
    "owner's_name": "jack sam",
}

pets = [curry,betty,kile]

for pet_name in pets:
    for key,value in pet_name.items():
        print(key.title() + ": " + value.title())
    print("\n")