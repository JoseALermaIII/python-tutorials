"""Regex version of strip()

This program acts like :meth:`str.strip` but using :py:mod:`re`.

Write a function, :meth:`regex_strip`, that takes a string and does the same thing
as the strip() string method.

If no other arguments are passed other than the string to strip, then
whitespace characters will be removed from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the function will be
removed from the string.

"""

import re


def regex_strip(text: str, replace: str = "") -> str:
    """Regex strip

    Implements the :meth:`str.strip` method using :py:mod:`re` by removing the given
    replace string in the given text.

    Args:
        text: String with text to remove given replace string from.
        replace: String to remove from given text. Defaults to empty string.

    Returns:
        String with replace string removed from text string.
    """
    if replace == "":
        whitespace_regex = re.compile(r"^\s+(\w+)\s+$")  #: Group characters between whitespace
        match = whitespace_regex.search(text)
        return match.group(1)
    else:
        sub_regex = re.compile(replace)  #: Match replacement text
        return sub_regex.sub("", text)


def main():
    message = "    something     "
    print(regex_strip(message))
    print(regex_strip(message, "some"))
    message = "Supercalifragilisticexpialidocious"
    print(regex_strip(message, "cali"))


if __name__ == '__main__':
    main()
