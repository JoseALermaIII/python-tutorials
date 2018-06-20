# Regex Version of strip() - this program acts like the strip() method but using regex
#
# Write a function that takes a string and does the same thing as the strip() string
# method. If no other arguments are passed other than the string to strip, then
# whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be
# removed from the string.
import re


def regex_strip(text, replace=""):
    if replace == "":
        whitespace_regex = re.compile(r"^\s+(\w+)\s+$")  # group characters between whitespace
        match = whitespace_regex.search(text)
        return match.group(1)
    else:
        sub_regex = re.compile(replace)  # match replacement text
        return sub_regex.sub("", text)


message = "    something     "
print(regex_strip(message))
print(regex_strip(message, "some"))
message = "Supercalifragilisticexpialidocious"
print(regex_strip(message, "cali"))
