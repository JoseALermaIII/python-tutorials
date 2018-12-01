# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.


def make_hashtable(nbuckets):
    hashtable = []
    for element in range(0, nbuckets):
        hashtable.append([])
    return hashtable


print(make_hashtable(12))
