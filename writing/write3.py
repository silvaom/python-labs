#!/usr/bin/python3.6 

#escritura
with open("writelines_outfiles.txt", "w") as f:
    f.writelines("%s\n" % i for i in range(10))

#lectura
with open("writelines_outfiles.txt", "r") as g:
    g.read()
