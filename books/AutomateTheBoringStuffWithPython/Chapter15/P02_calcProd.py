#! python3
#  P02_calcProd.py - Uses the time module to profile a function that calculates
#  the product of the first 100,000 numbers.

import time


def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
