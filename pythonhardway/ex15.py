# Import argument variables from sys module
from sys import argv

# argv holds 2 variables and we are assigning them to script and filename respectively
script, filename = argv

# Use the open command to open the text file
txt = open(filename)

# Print "Here's your file" with filename
print(f"Here's your file {filename}:")
# Call the command read on txt and print the content
print(txt.read())

# Print "Type the filename again:"
print("Type the filename again:")
# Print "> " and wait for user to input, and assign it to file_again
file_again = input("> ")

# Open file_again and assign to txt_again
txt_again = open(file_again)

# Call read on txt_again and print the content
print(txt_again.read())

txt.close()
txt_again.close()
