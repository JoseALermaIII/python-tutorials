# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(list_):
    new_list = zip(*list_) # Converts rows to columns in new list
    length = len(list_)
    i = 0
    # Debug list and new_list conversion
    #print("list: ", list_, "new_list: ", new_list)

    # Filters non-square lists
    while i < length:
        if len(list_[i]) != len(new_list[i]):
            return False
        i += 1

    # Compares lists
    i = 0
    while i < length:
        j = 0
        while j < len(list_[i]):
            # Debug list_[i][j], new_list[i][j], and comparison
            #print("list_[i][j]: ", list_[i][j],
            #      "new_list[i][j]: ", new_list[i][j],
            #      "result: ", list_[i][j] != new_list[i][j])
            if list_[i][j] != new_list[i][j]:
                return False
            j += 1
        i += 1
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False

print symmetric([[1, 2, 3],
                 [3, 1, 2],
                 [2, 3, 1]])
# >>> False
