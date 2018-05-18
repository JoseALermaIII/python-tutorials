# Chapter 10 Practice Questions

# 1. Which is correct: os.exists() or os.path.exists()?
import os
print(os.exists("PracticeQuestions.py"))
print(os.path.exists("PracticeQuestions.py"))

# 2. When is the Unix Epoch?
# Hint: check page 136
months = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October",
          "November", "December"]

month = 278 + 42 * 7 - 39 + 53 * 0 - 533
day = 153 * 7 - 1070
year = 394 * 5

print("The Unix Epoch is on %s %s, %s" % (months[month], day, year))

# 3. What do the following expressions evaluate to?
print('Foobar'.startswith('Foo'))
print('Foo'.startswith('Foobar'))
print('Foobar'.startswith('foo'))
print('bar'.endswith('Foobar'))
print('Foobar'.endswith('bar'))
print('The quick brown fox jumped over the yellow lazy dog.'.title())
