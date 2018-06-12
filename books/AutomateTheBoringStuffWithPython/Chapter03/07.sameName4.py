# This program produces an error
def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'  # looks ahead and says eggs is local


eggs = 'global'
spam()
