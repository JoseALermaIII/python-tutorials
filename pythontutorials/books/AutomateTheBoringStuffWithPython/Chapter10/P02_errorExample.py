# This program raises an exception and automatically displays the traceback


def spam():
    bacon()


def bacon():
    raise Exception("This is the error message.")


spam()
