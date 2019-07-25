jperson = {
    "first_name":"john",
    "last_name": "person",
    "age": 25,
    "city": "boston"
},
sjim = {
    "first_name":"simon",
    "last_name": "jim",
    "age": 28,
    "city": "washington"
},
kalice = {
    "first_name":"kelly",
    "last_name": "alice",
    "age": 23,
    "city": "los angeles"
},

people = [jperson,sjim,kalice]
for person in people:
    for quality in person:
        print("\n")
        for key, value in quality.items():
            print(key.title() + ": " + str(value).title())
