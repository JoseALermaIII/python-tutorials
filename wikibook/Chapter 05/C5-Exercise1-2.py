#!/usr/bin/env python3
# Write a program that asks the user of a Login Name and Password. Then when
# they type "lock", they need to type in their name and password to unlock  the
# program.

name = input('Set name: ')
password = input('Set password: ')
while 1 == 1:
    nameguess=""
    passwordguess=""
    key=""
    while (nameguess != name) or (passwordguess != password):
        nameguess = input('Name? ')
        passwordguess = input('Password? ')
    print("Welcome,", name, ". Type lock to lock.")
    while key != "lock":
        key = input("")
