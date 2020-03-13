#!/usr/bin/python3.8

#list all the content from a path passed as an argument
#call the script and passed the argument
from pathlib import Path
import sys 
#path = Path(sys.argv[1])

try: 
    path = Path(sys.argv[1])
    glob_path = path.glob('*')
    for file_path in glob_path:
        print(file_path)
except:
    print("Invalid argument. Type a valid directory")


    
