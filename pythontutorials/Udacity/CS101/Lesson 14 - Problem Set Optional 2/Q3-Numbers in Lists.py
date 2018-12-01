# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string_):
    list_ = [int(i) for i in string_] # Converts string to list
    # DEBUG: string to list conversion
    #print("\nstring: {} \nlist: {}".format(string_,list_))
    stack = []
    output = []
    previous = 0
    for current in list_:
        # DEBUG: variables and lists
        #print("""\nlist_: {} stack: {} output: {}
        #      \ncurrent: {} previous: {} current<=previous: {}""".format(list_,stack,output,
        #                                                                 current,previous,current<=previous))
        if current <= previous:
            stack.append(current)
        else:
            if stack:
                #print("\nStack {} to output {} before".format(stack,output)) # DEBUG: stack to output pre
                output.append(stack)
                #del stack[:] # BUG: del stack[:] breaks past and present references to stack. Feature?
                stack = [] # TODO: can use stack.clear() in Python 3.x?
                #print("Stack {} to output {} after".format(stack,output))  # DEBUG: stack to output post
            output.append(current)
            previous = current
    if stack: # stack at the end of the list
        output.append(stack)
    #print(output) # DEBUG
    return output

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
