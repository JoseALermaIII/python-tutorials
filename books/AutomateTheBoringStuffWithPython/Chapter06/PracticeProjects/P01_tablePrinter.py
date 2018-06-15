# This program displays a list of strings in a table
#
# Write a function named printTable() that takes a list of lists of strings and
# displays it in a well-organized table with each column right-justified. Assume
# that all the inner lists will contain the same number of strings.
#
# For example, the value could look like this:
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
#
# Your printTable() function would print the following:
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose


def printTable(matrix):
    # Calculate length of longest word in each row
    colWidths = []
    for row in matrix:
        maxWidth = 0
        for item in row:
            if len(item) > maxWidth:
                maxWidth = len(item)
        colWidths.append(maxWidth)

    # Sort lengths of words in each row and find longest word in matrix
    colWidths = sorted(colWidths)
    maxWidth = colWidths[-1]

    # Print each column with right-justification of longest word in matrix
    for index in range(len(matrix[0])):
        output = ""
        for row in matrix:
            output += row[index].rjust(maxWidth)
        print(output)


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)


if __name__ == "__main__":
    main()
