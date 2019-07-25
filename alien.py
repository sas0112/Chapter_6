# make an empty list for storing aliens
aliens = []

# make 30 aliens
for alien_number in range(30):
    new_alien = {"color":"red","points":5,"speed":"slow"}
    aliens.append(new_alien)

# make first 3 aliens green
for alien in aliens[:3]:
    if alien["color"] == "red":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "green"
        alien["speed"] = "fast"
        alien["points"] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))