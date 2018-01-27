# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

def check_sequence(list_):
    for element in list_:
        if isinstance(element, int) == False:
            return False
        if element < 1:
            return False
    temp = sorted(list_)
    return (len(temp) == (temp[-1] - temp[0] + 1))

def check_unique_digit(element, list_):
    return (element in range(min(list_), max(list_) + 1)) and (list_.count(element) == 1)

def check_rows(matrix):
    for row in matrix:
        if check_sequence(row) == False:
            return False
        for element in row:
            # Debug
            #print "Element: ", element, "Row: ", row, "Matrix: ", matrix
            if check_unique_digit(element, row) == False:
                return False
    return True

def check_columns(matrix):
    new_matrix = zip(*matrix)
    return check_rows(new_matrix)

def check_sudoku(square):
    return check_rows(square) and check_columns(square)

#
# Debug functions
#

def test_cs():
    # Debug check_sequence
    print "Begin check_sequence"
    print check_sequence([1, 2, 3, 4])
    print check_sequence([1, 1, 2, 3])
    print check_sequence([1, 2, 5, 4])
    print "End test check_sequence"

def test_cud():
    # Debug check_unique_digit
    print "Begin check_unique_digit"
    print check_unique_digit(1, [1, 2, 3, 4])
    print check_unique_digit(1, [1, 1, 3, 4])
    print check_unique_digit(5, [1, 2, 3, 4])
    print check_unique_digit(4, [1, 2, 3, 4])
    print "End test check_unique_digit"
    return

def test_cr():
    # Debug check_rows
    print "Begin check_rows"
    print check_rows(
            [[1, 2, 3, 4],
             [1, 1, 3, 4],
             [1, 2, 1, 4],
             [1, 2, 3, 1]])
    print check_rows(
            [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]])
    print check_rows(
            [[1, 2, 3, 4],
             [1, 2, 3, 4],
             [1, 2, 3, 4],
             [1, 2, 3, 4]])
    print check_rows(
            [[0, 1, 2],
             [2, 0, 1],
             [1, 2, 0]])
    print "End test check_rows"

def test_cc():
    # Debug check_columns
    print "Begin check_columns"
    print check_columns(
            [[1, 2, 3, 4],
             [1, 1, 3, 4],
             [1, 2, 1, 4],
             [1, 2, 3, 1]])
    print check_columns(
            [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]])
    print check_columns(
            [[1, 2, 3, 4],
             [1, 2, 3, 4],
             [1, 2, 3, 4],
             [1, 2, 3, 4]])
    print check_columns(
            [[1, 1, 1, 1],
             [2, 2, 2, 2],
             [3, 3, 3, 3],
             [4, 4, 4, 4]])
    print "End test check_columns"

#
# Begin main
#

#test_cs()
#test_cud()
test_cr()
#test_cc()

#print check_sudoku(incorrect)
# >>> False

#print check_sudoku(correct)
# >>> True

#print check_sudoku(incorrect2)
# >>> False

#print check_sudoku(incorrect3)
# >>> False

#print check_sudoku(incorrect4)
# >>> False

#print check_sudoku(incorrect5)
# >>> False
