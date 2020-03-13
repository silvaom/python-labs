#!/usr/bin/python3.8

#list all subdirectories using scandir

import os

basepath = '/home/omar.silva/Documents'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir:
            print(entry.name)
        else:
            print(f"{entry} is not a directory. It's a file")

