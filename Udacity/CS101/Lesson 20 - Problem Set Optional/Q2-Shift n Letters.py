# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
# negative or zero.


def shift_n_letters(letter, n):
    result = ord(letter) + n
    if result < ord('a'):
        return chr(ord('z') - (ord('a') - result) + 1)
    elif result > ord('z'):
        return chr(ord('a') + (result - ord('z')) - 1)
    else:
        return chr(result)


print(shift_n_letters('s', 1))
# >>> t
print(shift_n_letters('s', 2))
# >>> u
print(shift_n_letters('s', 10))
# >>> c
print(shift_n_letters('s', -10))
# >>> i
print(shift_n_letters('a', -3))
