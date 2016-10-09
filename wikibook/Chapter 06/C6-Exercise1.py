#!/usr/bin/env python3
# Write a program that asks the user their name, if they enter your name say
# "That is a nice name", if they enter "John Cleese" or "Michael Palin", tell
# them how you feel about them :),  otherwise tell them "You have a nice
# name."

name = input('Your name: ')
if name == 'Bryn':
    print('That is a nice name.')
elif name == 'John Cleese':
    print('... some funny text.')
elif name == 'Michael Palin':
    print('... some funny text.')
else:
    print('You have a nice name.')
