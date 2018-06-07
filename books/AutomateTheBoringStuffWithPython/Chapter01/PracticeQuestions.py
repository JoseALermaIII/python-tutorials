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



