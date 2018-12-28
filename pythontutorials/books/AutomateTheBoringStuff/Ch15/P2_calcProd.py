#! python3
"""Calculate product

Uses :py:mod:`time` to profile a function that calculates the product of the first 100,000 numbers.

Note:
    * Added :py:mod:`cProfile` for an execution profile. Does add overhead, so not suitable
      for benchmarking.
    * Added :py:mod:`timeit` for accurate execution timing.

"""

import time, cProfile, timeit


def calcProd() -> int:
    """Calculate product

    Calculates the product of the first 100000 integers using a :ref:`for <python:for>` loop.

    Returns:
        Integer product.
    """
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


def main():
    startTime = time.time()
    prod = calcProd()
    endTime = time.time()
    print('The result is %s digits long.' % (len(str(prod))))
    print('Took %s seconds to calculate.' % (endTime - startTime))

    time.sleep(1)

    cProfile.run('calcProd()')

    time.sleep(1)

    print(timeit.timeit('calcProd()', globals=globals()))  # doesn't finish - maxes out 2GB RAM


if __name__ == '__main__':
    main()
