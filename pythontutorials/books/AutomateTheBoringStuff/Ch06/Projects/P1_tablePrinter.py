"""Table printer

This program displays a list of strings in a table.

Write a function named :meth:`print_table` that takes a list of lists of strings and
displays it in a well-organized table with each column right-justified. Assume
that all the inner lists will contain the same number of strings.

For example, the value could look like this::

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

Your :meth:`print_table` function would print the following::

      apples Alice  dogs
     oranges   Bob  cats
    cherries Carol moose
      banana David goose

"""


def print_table(matrix: list) -> None:
    """Print table

    Prints given matrix with right justification based
    on the longest word in each row.

    Args:
        matrix: List of lists containing strings.

    Returns:
        None. Prints out matrix as table.
    """
    # Calculate length of longest word in each row
    col_widths = []
    for row in matrix:
        max_width = 0
        for item in row:
            if len(item) > max_width:
                max_width = len(item)
        col_widths.append(max_width)

    # Sort lengths of words in each row and find longest word in matrix
    col_widths = sorted(col_widths)
    max_width = col_widths[-1]

    # Print each column with right-justification of longest word in matrix
    for index in range(len(matrix[0])):
        output = ""
        for row in matrix:
            output += row[index].rjust(max_width)
        print(output)


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == "__main__":
    main()
