"""Regex search

Write a program that opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression.

The results should be printed to the screen.

"""


def main():
    import os, re

    # Get list of all .txt files
    all_files = os.listdir("./")  # use current working directory
    text_files = []
    for file in all_files:
        if file.endswith(".txt"):
            text_files.append(file)

    # Get regular expression
    regex = input("Enter regular expression to search for: ")
    search_regex = re.compile(regex)

    # Open .txt file
    for file in text_files:
        input_file = open(file)
        input_content = input_file.readlines()
        input_file.close()

        # Search for regex in file
        for line in input_content:
            match_objects = search_regex.findall(line)
            if match_objects is not None:
                # Print result
                for match in match_objects:
                    print(match)


if __name__ == '__main__':
    main()
