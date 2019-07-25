users = {
    'aeinstein':{
        'first':'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}


for user_name, user_info in users.items():
    print("\nUsername:" + user_name)
    full_name = user_info["first"].title() +" " + user_info["last"].title()
    location = user_info["location"].title()

    print('\tFull Name: ' + full_name)
    print('\tLocation:' + location)

print("hahaha")