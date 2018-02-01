the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print("This is count", number)

# Same as above
for fruit in fruits:
    print("A fruit of type", fruit)

# Also we can go through mixed lists too
for i in change:
    print("I got", i)

# We can also build lists, first start with an empty one
elements = range(0, 6)

# Now we can print them out too
for i in elements:
    print("Element was:", i)
