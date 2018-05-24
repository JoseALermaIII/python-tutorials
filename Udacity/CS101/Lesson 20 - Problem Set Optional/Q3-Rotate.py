# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(string_, shift):
    output = []
    for letter in string_:
        if letter == ' ':
            output.append(' ')
        else:
            output.append(shift_n_letters(letter, shift))
    return ''.join(output)


def shift_n_letters(letter, n):
    result = ord(letter) + n
    if result < ord('a'):
        return chr(ord('z') - (ord('a') - result) + 1)
    elif result > ord('z'):
        return chr(ord('a') + (result - ord('z')) - 1)
    else:
        return chr(result)


print(rotate ('sarah', 13))
# >>> 'fnenu'
print(rotate('fnenu', 13))
# >>> 'sarah'
print(rotate('dave', 5))
# >>>'ifaj'
print(rotate('ifaj', -5))
# >>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
# >>> ???
