#!/usr/bin/python3.8
#execute the script and pass it arguments
#python list-dir3.py /tmp

from pathlib import Path
import sys
path = Path(sys.argv[1])

glob_path = path.glob('*')

for file_path in glob_path:
    print(file_path)