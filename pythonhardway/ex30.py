# Initialise people to 30
people = 30
# Initialise cars to 40
cars = 40
# Initialise buses to 15
buses = 15

# If there are more cars then people
if cars > people:
    print("We should take the cars.")
# Else if there are less cars then people
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# If there are more buses than cars
if buses > cars:
    print("That's too many buses.")
# Else if there are less buses than cars
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

# If there are more people than buses
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
