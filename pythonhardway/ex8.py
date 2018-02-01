# Initialise formatter with 4 variables that can be inserted
formatter = "{} {} {} {}"

# Insert 1, 2, 3, 4 into formatter and print - prints 1 2 3 4
print(formatter.format(1, 2, 3, 4))
# Insert one, two, three, four into formatter and print - prints one two three four
print(formatter.format("one", "two", "three", "four"))
# Insert True False False True into formatter and print - prints True False False True
print(formatter.format(True, False, False, True))
# Inserts formatter 4 times into formatter - prints {} 16 times
print(formatter.format(formatter, formatter, formatter, formatter))
# Inserts 4 strings into formatter - prints the 4 strings separated by spaces
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
