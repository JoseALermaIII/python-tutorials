# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.


def shift(letter):
    if letter < 'z':
        return chr((ord(letter) + 1))
    return 'a'


print(shift('a'))
# >>> b
print(shift('n'))
# >>> o
print(shift('z'))
# >>> a
