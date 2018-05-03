# Chapter 9 Practice Questions

# 1. If you ran the following program and it printed the number 8, what would
#    it print the next time you ran it?
import random
random.seed(9)
print(random.randint(1, 10))
random.seed(9)
print(random.randint(1, 10))

# 2. What does the following program print?
spam = [1, 2, 3]
eggs = spam
ham = eggs
ham[0] = 99
print(ham == spam)

# 3. Which module contains the deepcopy() function?
# Hint: Check page 122...or the next question

# 4. What does the following program print?
import copy  # Don't do this, imports are supposed to be at the top of file
spam = [1, 2, 3]
eggs = copy.deepcopy(spam)
ham = copy.deepcopy(eggs)
ham[0] = 99
print(ham == spam)
