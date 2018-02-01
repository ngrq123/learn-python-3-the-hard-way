# Import argv in sys
from sys import argv

# Unpack argv into script and input_file
script, input_file = argv

# Define print_all function that takes in a file f
def print_all(f):
    # Print file contents
    print(f.read())

# Define rewind function that takes in a file f
def rewind(f):
    # Set stream position to be 0 (start of file)
    f.seek(0)

# Define print_a_line with line_count and file f
def print_a_line(line_count, f):
    # Print line_count and line read from file
    print(line_count, f.readline(), end='')

# Open input_file (unpacked from argv)
current_file = open(input_file)

# Print "First let's print the whole file" with a line break
print("First let's print the whole file:\n")

# Call print_all with the file argument, file contents will be printed
print_all(current_file)

# Print "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

# Call rewind with the file as argument, file stream will be set to the beginning
rewind(current_file)

# Print "Let's print three lines:"
print("Let's print three lines:")

# Initialise current_line as 1
current_line = 1
# Call print a line with current_line and current_file as arguments, first line will be printed
print_a_line(current_line, current_file)

# Add 1 to current_line
current_line += 1
# Call print a line with current_line and current_file as arguments, second line will be printed
print_a_line(current_line, current_file)

# Add 1 to current line
current_line += 1
# Call print_a_line with current_line and current_file as arguments, third line will be printed
print_a_line(current_line, current_file)
