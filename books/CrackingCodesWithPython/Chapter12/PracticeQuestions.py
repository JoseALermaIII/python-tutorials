# Chapter 12 Practice Questions

# 1. What does this expression evaluate to?
expression = '    Hello world'.strip()
print(expression)

# 2. Which characters are whitespace characters?
# Hint: Check page 145
print("Answer: These are the whitespace characters in Python.")
print("What are ' ', '\\t', and '\\n'?")
print("Ooh, I'm sorry, we were looking for their names, not characters.")

# 3. Why does 'Hello world'.strip('o') evaluate to a string that still has Os
#    in it?
expression = 'Hello world'.strip('o')
print(expression)
expression = 'oooHello worldooo'.strip('o')
print(expression)

# 4. Why does 'xxxHelloxxx'.strip('X') evaluate to a string that still has Xs
#    in it?
expression = 'xxxHelloxxx'.strip('X')
print(expression)
expression = 'XXXHelloXXX'.strip('X')
print(expression)
