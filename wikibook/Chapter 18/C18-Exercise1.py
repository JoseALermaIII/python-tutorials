#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# Update at least the phone numbers program (in section Dictionaries) so it
# doesn't crash if a user doesn't enter any data at the menu.
def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    try:
        menu_choice = int(input("Type in a number (1-5): "))
        if menu_choice == 1:
            print("Telephone Number:")
            for x in numbers.keys():
                print("Name: ", x, "\tNumber:", numbers[x])
                print()
        elif menu_choice == 2:
            print("Add Name and Number")
            name = input("Name: ")
            phone = input("Number: ")
            numbers[name] = phone
        elif menu_choice == 3:
            print("Remove Name and Number")
            name = input("Name: ")
            if name in numbers:
                del number[name]
            else:
                print(name, "was not found")
        elif menu_choice == 4:
            print("Lookup Number")
            name = input("Name: ")
            if name in numbers:
                print("The number is", numbers[name])
            else:
                print(name, "was not found")
        elif menu_choice != 5:
                print_menu()
    except ValueError:
        print("Need to use a number (1-5).\n")
