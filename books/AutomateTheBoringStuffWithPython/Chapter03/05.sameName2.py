# This program has only one variable
def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)
