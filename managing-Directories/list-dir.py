import os

path = "/home/omar.silva/Documents"

with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)
        