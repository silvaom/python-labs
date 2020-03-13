#!/usr/bin/python3.8

with open('dog_breeds.txt', 'r') as reader:
    #read and print the entire file line by line
    line = reader.readline()
    while line != '': # the eof char is an empty string
        print(line, end='')
        line = reader.readline()