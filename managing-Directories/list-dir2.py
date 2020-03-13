#!/usr/bin/python3.8
def list_dirs(basepath='/tmp'):
    """listing all directories in a dir"""
    entries = Path(basepath)
    for entry in entries.iterdir():
        print(entry.name)


if __name__ == "__main__":
    from pathlib import Path
    print("Type in the desire directory. All directories will be listed")
    print("Default directory is /tmp")
    basepath = input("Example: /tmp\n")
    list_dirs()
    
    
    