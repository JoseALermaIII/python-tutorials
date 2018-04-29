# Is each spam a global or local variable?

spam = 42  # global/local


def foo():
    global spam
    spam = 99  # global/local
    print (spam)


foo()  # mind == blown
