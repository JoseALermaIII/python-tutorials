# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.
def measure_udacity(in_list):
    count = 0

    for element in in_list:
        if element[0] == 'U':
            count += 1
        continue

    return count

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
