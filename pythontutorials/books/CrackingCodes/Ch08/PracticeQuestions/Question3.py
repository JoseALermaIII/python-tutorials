"""Chapter 8 Practice Question 3

Draw the complete truth tables for the and, or, and not operators.
"""


def notTruthTable() -> None:
    """Not truth table.

    Prints a truth table for the not operator.

    Returns:
         None. Only prints out a table.
    """
    print(" _________________________\n",
          "|not A    | Evaluates to:|\n",
          "|_________|______________|\n",
          "|not False| True         |\n",
          "|not True | False        |\n",
          "|_________|______________|\n")
    return None


def andTruthTable() -> None:
    """And truth table.

    Prints a truth table for the and operator.

    Returns:
         None. Only prints out a table.
    """
    print(" _______________________________\n",
          "|A and B        | Evaluates to:|\n",
          "|_______________|______________|\n",
          "|False and False| False        |\n",
          "|False and True | False        |\n",
          "|True and False | False        |\n",
          "|True and True  | True         |\n",
          "|_______________|______________|\n")
    return None


def orTruthTable() -> None:
    """Or truth table.

    Prints a truth table for the or operator.

    Returns:
         None. Only prints out a table.
    """
    print(" ______________________________\n",
          "|A or B        | Evaluates to:|\n",
          "|______________|______________|\n",
          "|False or False| False        |\n",
          "|False or True | True         |\n",
          "|True or False | True         |\n",
          "|True or True  | True         |\n",
          "|______________|______________|\n")
    return None


def main():
    notTruthTable()
    andTruthTable()
    orTruthTable()


# If Question3.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()
