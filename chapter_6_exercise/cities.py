cities = {
    "beijing": {
        "country": "china",
        "population": "21.54m",
        "fact": "The city is rich in traditional chinese culture and it "
                "contains a lot of treasure good and places of interest",
    },
    "shanghai":{
        "country": "china",
        "population": "21.54m",
        "fact": "The city has a lot of modern public transport along with"
                " more westernized lifestyle",
    },
    "tokyo": {
        "country": "japan",
        "population": "13,50m",
        "fact": "The city is very densely populated and all the infrastructures"
                " are pretty compact, but modern and clean",
    },
}

for city,city_features in cities.items():
    print("Here are some of the features about the city of " + city.title() + ":")
    for key,value in city_features.items():
        if value != "fact":
            print("\t" + key.title() + ": "+ value.title())
        else:
            print("\t" + key.title() + ": "+ value)
    print("\n")