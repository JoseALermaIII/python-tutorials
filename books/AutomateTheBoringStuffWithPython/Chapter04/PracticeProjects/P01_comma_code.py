# This program converts a list to a comma separated string
#
# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item.
#
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# For example, passing the previous spam list to the function would return
# 'apples, bananas, tofu, and cats'. But your function should be able to work
# with any list value passed to it.
import copy


def to_string(input_list):
    temp_list = copy.copy(input_list)  # Don't modify input_list
    temp_list.insert(-1, "and ")
    for index in range(0, len(temp_list) - 2):
        temp_list[index] += ', '
    return ''.join(temp_list)


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(to_string(spam))
    spam = ['lions', 'tigers', 'bears']
    print(to_string(spam) + ". Oh, my!")


if __name__ == '__main__':
    main()
