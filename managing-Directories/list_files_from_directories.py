#!/usr/bin/python3.6 
 
import os

#list all files in a directory using os.listdir

basepath = '/home/omar.silva/Documents/Python'

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
