# This program demonstrates how mutable data types are passed to functions
def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)
