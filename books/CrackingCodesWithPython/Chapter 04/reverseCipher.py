# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Note: pretty much the same, except I use double quotes,
# expand variable names for readability, simplify the while loop,
# and use fancier operators

message = "Three can keep a secret, if two of them are dead."
#message = input("Enter message: ")  # Allow users to enter message
translated = ""

index = len(message)
while index:
    index -= 1  # equivalent to index = index - 1
    translated += message[index]
    #print("index is", i, ", message[index] is", message[index], ", translated is", translated)  #DEBUG

print(translated)

# Decrypt example
# Was going to make a function out of it so it's easier, but I
# didn't want to change it more than I already did. (^_^;)
#print(translated[::-1])  # a step of -1 reverses the string
