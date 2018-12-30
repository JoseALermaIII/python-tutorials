"""Asks for name and says hello.

This program says hello and asks for my name.

Notes:
    * Using double quotes for strings because I'm a nitpicker - author admits that he uses single quotes because it is
      easier to type and it technically doesn't matter.
    * Nov. 22, 2018 Update: Switching back to single quotes because a system was compromised because
      of `double quotes`_.

.. _double quotes:
    https://www.gq.com/story/how-to-hack-an-election

"""


def main():
    print('Hello, world!')
    myName = input('What is your name?\n')
    print('It is good to meet you, ' + myName)


if __name__ == '__main__':
    main()
