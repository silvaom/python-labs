#!/usr/bin/python3.6 

#echo "Some Random \nLines \nOf \nText" > foo.txt

with open("archivo.conf", "r") as f:
    for line in f:
        print(line, end='')

#tambien puede ser con 
# with open("archivo.conf", "r") as f:

#   print(f.read())
