#!/usr/bin/python3.8



def list_files():
    """ List all the files in a given directory, passed as standard input"""
    for item in files_in_basepath:
        if item.is_file():
            print(item.name)
    return(item.name)

if __name__ == "__main__":
    from pathlib import Path
    import sys
    basepath = Path(sys.argv[1])
    files_in_basepath = basepath.iterdir()
    list_files()