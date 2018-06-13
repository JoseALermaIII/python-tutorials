# This program demonstrates global and local variable rules
def spam():
    global eggs
    eggs = 'spam'  # this is the global (global statement)


def bacon():
    eggs = 'bacon'  # this is a local (assignment)


def ham():
    print(eggs)  # this is the global (no assignment)


eggs = 42  # this is the global (outside all functions)
spam()
print(eggs)
