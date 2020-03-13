#!/usr/bin/python3.8

#listing all files in a directory using os.scandir()

import os
basepath='/home/omar.silva/Documents'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file(): #returns true if the object is a file
            print(entry.name)
