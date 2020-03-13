#!/usr/bin/env python
#function searches for a given pattern on a given file and counts the number of ocurrences and the number of lines of the file
#this is the compile version. better performance the the regular one
import re

def run_re():
    pattern = '([a-z][A-Z])'
    re_obj = re.compile(pattern)

    infile = open('dotfiles.txt', 'r')
    match_count = 0 
    lines = 0 
    for line in infile:
        match = re_obj.search(line)
        if match:
            match_count+= 1
        lines += 1
    return (lines, match_count)

if __name__ == "__main__":
    lines, match_count = run_re()
    print(f'N° OF LINES::', {lines})
    print(f'N° OF MATCHES::', {match_count})
