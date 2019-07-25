favorite_langauges = {
    'jen' : ['python','ruby'],
    'sarah': ['c','go'],
    'ben': ['ruby','c++'],
    'phil': ['haskell','java'],
}

for name, langauges in favorite_langauges.items():
    print("\n" + name.title() + "'s favorite langauges are:")
    for language in langauges:
        print(language)