# Password checker
typedPassword = input("Enter your password.\n")
if typedPassword == "hunter2":
    print("You entered: *******")
elif typedPassword == "jose":
    print("Hint: the password is a meme.")
elif typedPassword == "12345":
    print("That is a really obvious password.")
else:
    print("You entered: " + typedPassword)
print("Done")
