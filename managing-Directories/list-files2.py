#!/usr/bin/python3.8

#not working
def list_files():
    """ List files on a given directory"""
    file_in_basepath = basepath.iterdir()
    for item in file_in_basepath:
        if item.is_file():
            print(item.name)

if __name__ == "__main__":
    from pathlib import Path
    print("Type in the directory. Files inside the directory will be listed")
    basepath = input("Ejemplo: /tmp\n")
    list_files()