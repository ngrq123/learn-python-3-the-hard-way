# Assign 100 to cars
cars = 100
# Assign 4 as the number of space in the car
space_in_the_car = 4.0
# Assign 30 to drivers
drivers = 30
# Assign 90 to passengers
passengers = 90
# Assign the difference of cars and drivers to cars not driven
cars_not_driven = cars - drivers
# Assign number of drivers to cars driven
cars_driven = drivers
# Assign cars driven multiply by space in the car to carpool capacity
carpool_capacity = cars_driven * space_in_the_car
# Assign passengers divided by cars driven to average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
