#!/usr/bin/python

import time
def calcProd():
    product = 1
    for i in range(1,1000):
        product = product * i

startTime = time.time()
prod = calcProd()
endTime = time.time()
print (f'the result is {len(str(prod))}')
print (f'Took  {endTime - startTime} seconds to calculate. ')

