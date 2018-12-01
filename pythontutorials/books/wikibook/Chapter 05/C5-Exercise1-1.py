#!/usr/bin/env python3
# Write a program that asks the user of a Login Name and Password. Then when
# they type "lock", they need to type in their name and password to unlock  the
# program.

name = input("What is your UserName: ")
password = input("What is your Password: ")
print("To lock your computer type lock.")
command = None
input1 = None
input2 = None
while command != "lock":
    command = input("What is your command: ")
while input1 != name:
    input1 = input("What is your username: ")
while input2 != password:
    input2 = input("What is your password: ")
print("Welcome back to your system!")
