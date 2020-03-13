#!/usr/bin/python  
#works with 2 files a the same time
# opens 1 files and writes to another

source_path = 'dog_breeds.txt'
destiny_path = 'dog_breeds_reversed.txt'
with open(source_path, 'r') as reader, open(destiny_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))