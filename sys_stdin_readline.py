#!/usr/bin/python3.6

#Enumerating sys.stdin.readline
import sys

counter = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    print ("%s: %s" %(counter, line))
    counter += 1