#!/usr/bin/python3.8

import sys, getopt

#Store input and output filenames
ifile=''
ofile=''

#read command line args
myopts, args = getopt.getopt(sys.argv[1:], "i:o:")
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    else:
        print(f"Usage: {sys.argv[0]} -i input -o output ")

#Display input and output file name passed as the args
print(f"input file is : {ifile}, and output file is: {ofile}")
         