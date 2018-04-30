# What do the following pieces of code display on the screen?

# a
spam = "foo"
for i in spam:
    spam = spam + i
print(spam)

# b
if 10 < 5:
    print("Hello")
elif False:
    print("Alice")
elif 5 != 5:
    print("Bob")
else:
    print("Goodbye")

# c
print("f" not in "foo")

# d
print("foo" in "f")

# e
print("hello".find("oo"))
