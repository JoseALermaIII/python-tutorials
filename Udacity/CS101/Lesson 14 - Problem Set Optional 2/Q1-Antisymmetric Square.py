# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(list_):
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
            if list_[i][j] != -new_list[i][j]:
                return False
            j += 1
        i += 1
    return True


# Test Cases:

print antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]])
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
