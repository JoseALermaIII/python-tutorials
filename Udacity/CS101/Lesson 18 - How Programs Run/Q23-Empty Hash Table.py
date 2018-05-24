# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.


def make_hashtable(nbuckets):
    hashtable = []
    count = 0
    while count < nbuckets:
        hashtable.append([])
        count += 1
    return hashtable


print(make_hashtable(12))
