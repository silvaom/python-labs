#!/usr/bin/python3.6

#Enumerating sys.stdin.readline
import sys

counter = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    #print "%s: %s" % (counter, line)
    print(f"{counter}, {line}")
    counter += 1
    end = input("Would you like to end? Type 'yes' or 'no' \n")
    if end == 'yes':
        break
    else:
        print("Keep on typing then\n")