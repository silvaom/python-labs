#!/usr/bin/python3.6 

#The following is an example 
#that shows you how to list all files and directories in a directory tree using os.walk().

import os
basepath = '/home/omar.silva/Documents/Python'

for dirpath, dirnames, files in os.walk(basepath):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)