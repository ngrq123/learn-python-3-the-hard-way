# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print(f"Copying from {from_file} to {to_file}")
#
# # We could do these two on one line too, how?
# indata = open(from_file).read()
#
# print("Ready, hit RETURN to continue. CTRL-C to abort.")
# input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print("Alright, all done.")
#
# out_file.close()

from sys import argv

script, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())
