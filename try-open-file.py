#!/usr/bin/python3.6 

try:
    f = open('writeable.txt', 'w')
    f.write('just a quick line here\n')
finally:
    f.close()