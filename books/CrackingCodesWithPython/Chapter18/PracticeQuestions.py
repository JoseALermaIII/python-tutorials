# Chapter 18 Practice Questions

# 1. Which cipher is the Vigenère cipher similar to, except that the Vigenere
#    cipher uses multiple keys instead of just one key?
# Hint: Check page 248
from books.CrackingCodesWithPython.Chapter18.vigenereCipher import decryptMessage

message = "Tuw Rmxeawni Ticzav zs faimcae lk xye Psawrr pallvr."  # Encrypted with ANSWER
#print(decryptMessage(blank, blank))  # Fill in the blanks

# 2. How many possible keys are there for a Vigenère key with a key length
#    of 10?
# Hint: Check page 250
#
# a. Hundreds
# b. Thousands
# c. Millions
# d. More than a trillion
from math import pow  # Don't do this - imports should be at the top of the file
solution = pow(26, 10)
answer = "Undefined"
if solution <= 999:
    answer = "a. Hundreds"
elif 999 < solution <= 9999:
    answer = "b. Thousands"
elif 999999 < solution <= 999999999:
    answer = "c. Millions"
elif solution > 1000000000:
    answer = "d. More than a trillion"
else:
    print("404: Answer not found (;_;)")

#print("%s: %s" % (answer, solution))

# 3. What kind of cipher is the Vigenère cipher?
# Hint: Check page 248

message = "Mft Zbetrxpt Gbnwik gh e imactjeltztxba hyuqimmsimhl rmiftv."  # Encrypted with TYPE
#print(decryptMessage(blank, blank))  # Fill in the blanks
