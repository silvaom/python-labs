#!/usr/bin/python3.8

from pathlib import Path

#list all directories using pathlib

basepath = Path('/home/omar.silva/Documents')

for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
    

