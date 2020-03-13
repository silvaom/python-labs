#!/usr/bin/python3.6 

#prints directories

import os
basepath = '/home/omar.silva'

entries = os.listdir(basepath)

for dir in entries:
    print(dir)