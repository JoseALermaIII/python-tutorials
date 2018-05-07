# Chapter 13 Practice Questions

# 1. What do the following expressions evaluate to?
print(17 % 1000)
print(5 % 5)

# 2. What is the GCD of 10 and 15?
# Don't do this - imports should be at the top of the file
from books.CrackingCodesWithPython.Chapter13.cryptomath import gcd
print(gcd(10, 15))

# 3. What does spam contain after executing spam, eggs = 'hello', 'world'?
spam, eggs = 'hello', 'world'
print(spam)

# 4. The GCD of 17 and 31 is 1. Are 17 and 31 relatively prime?
if not gcd(17, 31) == 1:
    print("No")
else:
    print("Yes")

# 5. Why aren't 6 and 8 relatively prime?
print(gcd(6, 8))

# 6. What is the formula for the modular inverse of A mod C?
# Hint: check page 183
