favorite_langauges = {
    'jen': ['python','ruby'],
    'sarah': ['c','go'],
    'ben': ['ruby','c++'],
    'phil': ['haskell','java'],
}

for name, languages in favorite_langauges.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print(language)