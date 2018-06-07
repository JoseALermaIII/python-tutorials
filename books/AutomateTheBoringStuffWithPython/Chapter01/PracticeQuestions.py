# Chapter 1 Practice Questions

# 1. Which of the following are operators, and which are values?
# Hint: Check location 28.6
# *
# 'hello'
# -88.8
# -
# /
# +
# 5
items = ['*', "hello", -88.8, '-', '/', '+', 5]
for item in items:
    if str(item) not in "*-/+":
        print("%s is a value." % item)
    else:
        print("%s is an operator." % item)

# 2. Which of the following is a variable, and which is a string?
# Hint: Check locations 33.8 and 37.0
# spam
# 'spam'
spam = {"spam": True}
items = [spam, 'spam']
for item in items:
    if not isinstance(item, str):
        print("%s has to be a variable." % item)
    else:
        print("'%s' is definitely a string." % item)

# 3. Name three data types
# Hint: Check location 33.8
data = [124, 42.2, '\_(&_&)_/']
for element in data:
    print(type(element))

