# Define a fucntion cheese_and_crackers with two arguments: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print cheese_count
    print(f"You have {cheese_count} cheeses!")
    # Print boxes_of_crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Print "Man that's enough for a party!"
    print("Man that's enough for a party!")
    # Print "Get a blanket" with a line break
    print("Get a blanket.\n")

# Print "We can just give the function numbers directly:"
print("We can just give the function numbers directly:")
# Call cheese_and_crackers with cheese_count 20 and boxes_of_crackers 30
cheese_and_crackers(20, 30)

# Print "OR, we can use variables from our script:"
print("OR, we can use variables from our script:")
# Initialise amount_of_cheese to 10
amount_of_cheese = 10
# Initialise amount_of_crackers to 50
amount_of_crackers = 50

# Call cheese_and_crackers with cheese_count 10 and boxes_of_crackers 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print "We can even do math inside too:"
print("We can even do math inside too:")
# Call cheese_and_crackers with cheese_count 30 and boxes_of_crackers 11
cheese_and_crackers(10 + 20, 5 + 6)

# Print "And we can combine the two, variables and math:"
print("And we can combine the two, variables and math:")
# Call cheese_and_crackers with cheese_count 110 and amount_of_crackers 1050
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
