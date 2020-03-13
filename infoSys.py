#!/usr/bin/python
# script to gather information about the system

import subprocess

#print system information

def uname_func():
    
    uname = 'uname'
    uname_arg = '-a'
    print(f'System info from {uname} :' )
    subprocess.call([uname, uname_arg])

def directory_space():
    usage = 'du'
    usage_arg = '-h'
    path = '/etc'
    print(f'Space used in the {path} directory')
    subprocess.call([usage, usage_arg, path])


def disk_func():
    
    diskspace = 'df'
    diskspace_arg = '-h'
    print(f'This is like using the {diskspace} command')
    subprocess.call([diskspace, diskspace_arg])

#main func that calls the others functions
def main():
    uname_func()
    disk_func()
    directory_space()

if __name__ == "__ main__":
    main()


