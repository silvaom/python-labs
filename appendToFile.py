#!/usr/bin/python  
#appends to a file. just add a 'a' for the mode argument

with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')
