#!/usr/bin/python3.6 
 
from pathlib import Path
#list all subdirectories using pathlib

basepath = Path('/home/omar.silva/Documents/Python')

for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
        
