#!/usr/bin/python3.8

import sys, getopt

#Store input and output filenames
ifile=''
ofile=''

#read command line args
myopts, args = getopt.getopt(sys.argv[1:], "i:o:")
