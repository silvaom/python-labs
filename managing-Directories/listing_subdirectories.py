#!/usr/bin/python3.6 
 
import os

#list all subdirectories using scandir()

basepath = '/home/omar.silva/Documents/Python'

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
           print(entry.name)
          
             
            
            
    
    
