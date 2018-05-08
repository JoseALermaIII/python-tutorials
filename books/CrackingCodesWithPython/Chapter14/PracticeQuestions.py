# Chapter 14 Practice Questions

# 1. The affine cipher is the combination of which two other ciphers?
# Hint: Check page 171 or 185
print("Answer: The affine cipher is comprised of these two ciphers.")
print("What are the times cipher and the salad cipher?")
print("Ooh, I'm sorry, but we were looking for the proper names.")
print("(╯°□°)╯︵ ┻━┻\n")

# 2. What is a tuple? How is a tuple different from a list?
# Hint: Check page 190
sampleTuple = (1, 4, 6)
print(sampleTuple[2])
#sampleTuple[2] = 5  # Uncomment this line, I dare you


# 3. If Key A is 1, why does it make the affine cipher weak?
# Hint: Check page 190
SYMBOLS = "ABC"
keyA = 1
print(SYMBOLS.find('C') * keyA)

# 4. If Key B is 0, why does it make the affine cipher weak?
# Hint: Check page 190
keyB = 0
print(SYMBOLS.find('C') * keyA + keyB)
