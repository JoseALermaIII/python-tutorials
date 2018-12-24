"""Mad libs

Create a Mad Libs program that reads in text files and lets the user add their own
text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

For example, a text file may look like this::

    The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
    unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

::

    Enter an adjective:
    silly
    Enter a noun:
    chandelier
    Enter a verb:
    screamed
    Enter a noun:
    pickup truck

The following text file would then be created::

    The silly panda walked to the chandelier and then screamed. A nearby pickup
    truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
"""


def main():
    import re

    # Read input file
    input_file = open("madlibs_input.txt")
    input_content = input_file.readlines()
    input_file.close()

    # Open output file
    output_file = open('madlibs_output.txt', 'w')

    # Check for keywords and prompt for input
    keywords = ["ADJECTIVE", "ADVERB", "NOUN", "VERB"]
    keyword_regex = re.compile(r"[A-Z]{4,9}")  # uppercase words 4-9 characters long
    for line in input_content:
        match = -1
        while match is not None:
            match = keyword_regex.search(line)
            # Replace keywords and write to new file
            if match is not None and match.group() in keywords:
                if match.group()[0].lower() == 'a':
                    replace = input("Enter an %s: " % match.group().lower())
                else:
                    replace = input("Enter a %s: " % match.group().lower())
                line = line.replace(match.group(), replace, 1)
        output_file.write(line)
        print(line)
    output_file.close()


if __name__ == '__main__':
    main()
