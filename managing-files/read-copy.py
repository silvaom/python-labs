from sys import argv
from os.path import exists

source = input("Which file would you like to copy\n")
destiny = input("Name of the new file?:\n")



print(f"Copying from {source}, to {destiny}")
in_file = open(source)

indata = in_file.read()

longitud = len(indata)
print(f"The input file is {longitud} bytes long")
answer = exists(destiny)

print(f"Does the output file exists ? {answer}") 
print("Ready, hit return to continue. Or CTRL-C to cancel")
input()

out_file = open(destiny, 'w')
out_file.write(indata)

print("Operation finished")

out_file.close()
in_file.close()


