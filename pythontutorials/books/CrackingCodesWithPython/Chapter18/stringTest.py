"""Create string test

Timing string concatenation vs list appending to make a string.

Note:
    * Prints time to make a 10000 character string 10000 times as seconds since the Unix epoch.

"""

import time


def main():
    startTime = time.time()
    for trial in range(10000):
        building = ''
        for i in range(10000):
            building += 'x'
    print('String concatenation: ', (time.time() - startTime))

    startTime = time.time()
    for trial in range(10000):
        building = []
        for i in range(10000):
            building.append('x')
        building = ''.join(building)
    print('List appending:       ', (time.time() - startTime))


if __name__ == '__main__':
    main()
