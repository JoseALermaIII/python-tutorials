# This program uses the csv module to manipulate .csv files

import csv

# Writer Objects
outputFile = open("output.csv", "w", newline='')
outputWriter = csv.writer(outputFile)
print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
print(outputWriter.writerow([1, 2, 3.141592, 4]))
outputFile.close()
