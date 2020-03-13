#!/usr/bin/python3.6
#this is a better aproach
#readlines() returns a list where each element in the list reprsents a line in the file
with open('dog_breeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')
        
#simpler 
# Read and print the entire file line by line

#with open('dog_breeds.txt', 'r') as reader:
#   for line in reader:
#       print(line, end='')