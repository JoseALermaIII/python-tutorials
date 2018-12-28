"""Write CSV

This program uses :py:mod:`csv` to write .csv files.

Note:
    Creates 'output.csv' and 'example.tsv' files.

"""


def main():
    import csv

    # Writer Objects
    outputFile = open("output.csv", "w", newline='')
    outputWriter = csv.writer(outputFile)
    print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
    print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
    print(outputWriter.writerow([1, 2, 3.141592, 4]))
    outputFile.close()

    # Delimiter and lineterminator Keyword Arguments
    csvFile = open("example.tsv", 'w', newline='')
    csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
    print(csvWriter.writerow(['apples', 'oranges', 'grapes']))
    print(csvWriter.writerow(['eggs', 'bacon', 'ham']))
    print(csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam']))
    csvFile.close()


if __name__ == '__main__':
    main()
