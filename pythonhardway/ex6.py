# Initialise types of people to 10
types_of_people = 10
# Insert 10 in the string
x = f"There are {types_of_people} types of people."

# Initialise binary as "binary"
binary = "binary"
# Initialise do_not as "don't"
do_not = "don't"
# Insert binary and do_not in string
y = f"Those who know {binary} and those who {do_not}."

# Print "There are 10 types of people"
print(x)
# Print "Those who know binary and those who don't"
print(y)

# Print "I said: There are 10 types of people"
print(f"I said: {x}")
# Print "I also said: Those who know binary and those who don't"
print(f"I also said: {y}")

# Initialise hilarious as False
hilarious = False
# Initialise joke_evaluation as "Isn't that joke so funny?!" with an empty variable behind
joke_evaluation = "Isn't that joke so funny?! {}"

# Print "Isn't that joke so funny? False"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
