#!/usr/bin/env python
import sys

print('ahora debe ingresar texto')

for i, line in enumerate(sys.stdin):
    print ("%s: Lo que ingreso fue: %s" % (i, line))