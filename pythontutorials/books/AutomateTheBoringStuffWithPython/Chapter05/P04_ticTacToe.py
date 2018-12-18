"""Tic Tac Toe

This program plays a game of tic-tac-toe using a :obj:`dict` to store the board.

Attributes:
    theBoard (dict): Dictionary containing the current status of the tic-tac-toe board.

Note:
    * Space names are defined as follows::
    
        top-L | top-M | top-R
        ------+-------+------
        mid-L | mid-M | mid-R
        ------+-------+------
        low-L | low-M | low-R

    * Intended for two players.

"""

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board: dict) -> None:
    """Print board
    
    Prints each row of a given tic-tac-toe board.
    
    Args:
        board:  Dictionary containing space names as keys and contents as values.

    Returns:
        None. Prints rows of tic-tac-toe board.
    """
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def main():    
    turn = 'X'
    """char: Player's marker, either `X` or `O`"""

    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)


if __name__ == '__main__':
    main()
