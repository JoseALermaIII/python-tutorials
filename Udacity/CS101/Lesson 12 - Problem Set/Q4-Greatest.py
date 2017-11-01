# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


def greatest(list_of_numbers):
    greater = 0

    if list_of_numbers is False:
        return 0

    for element in list_of_numbers:
        if element > greater:
            greater = element
    return greater

print greatest([4,23,1])
# >>> 23
print greatest([])
# >>> 0
