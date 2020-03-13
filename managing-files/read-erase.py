from sys import argv
from os.path import exists

filename = input("Name of the file?:")
print(">")
print(f"We are goint to erase {filename}\n")

print("if you do want that, print return")
print("If you dont want that, hit ctrl-c ")

print(f"Opening the file {filename}")
target = open(filename, 'w')

print("Truncating the file")
target.truncate()

print("Please write three lines")

line1 = input("line 1:\n")
line2 = input("Line 2:\n")
line3 = input("Line 3:\n")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print ("And finally close the file")
target.close()
