# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

def list_mean(list_):
    sum_ = 0
    if not list_:
        raise TypeError
    for element in list_:
        sum_ += element
    return float(sum_) / len(list_)

print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0