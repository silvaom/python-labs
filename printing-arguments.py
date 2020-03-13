#!/usr/bin/python3.8

import sys

#get the total number of args passed to this script
total = len(sys.argv)

#get the arguments list
cmdargs = str(sys.argv)

print(f"The total number of args passed to the script is: {total}")
print(f"Args list: {cmdargs}")
print(f"The name of this script is: {sys.argv[0]}")
for i in range(total):
    print(f"Argument #{i} is: {str(sys.argv[i])} ")