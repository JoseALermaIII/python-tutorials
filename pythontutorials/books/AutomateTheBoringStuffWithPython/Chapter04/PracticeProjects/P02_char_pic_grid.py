"""Character Picture Grid

This program converts a matrix to an image.

Say you have a list of lists where each value in the inner lists is a one-character string, like this::

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

You can think of `grid[x][y]` as being the character at the x- and y-coordinates of a “picture” drawn
with text characters. The `(0, 0)` origin will be in the upper-left corner, the x-coordinates increase
going right, and the y-coordinates increase going down.

Copy the previous grid value, and write a function, :meth:`matrix_to_pic`, that uses it to print the image::

    ..OO.OO..
    .OOOOOOO.
    .OOOOOOO.
    ..OOOOO..
    ...OOO...
    ....O....

"""


def matrix_to_pic(matrix: list) -> None:
    """Matrix to picture

    Converts a matrix of lists with one-character values into `ASCII Art`_.

    Args:
        matrix: List with lists containing one-character elements.

    Returns:
         None. Prints the contents of the lists as `ASCII Art`_

    .. _ASCII Art:
        https://en.wikipedia.org/wiki/ASCII_art
    """
    new_matrix = zip(*matrix)  #: Convert rows to columns in new matrix
    for item in new_matrix:
        print(''.join(item))
    return None


def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    matrix_to_pic(grid)


if __name__ == "__main__":
    main()
