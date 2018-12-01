#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

max_points = [25, 25, 50, 25, 100]
assignments = ['hw ch1', 'hw ch 2', 'quiz    ', 'hw ch 3', 'test ']
students = {'#Max': max_points}

def print_menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Print grades")
    print("4. Record grade")
    print("5. Print Menu")
    print("6. Exit")

def print_all_grades():
    print('\t', end=' ')
    for i in range(len(assignments)):
        print(assignments[i], '\t', end=' ')
    print()
    keys = list(students.keys() )
    keys.sort()
    for x in keys:
        print(x, '\t', end=' ')
        grades = students[x]
        print_grades(grades)

def print_grades(grades):
    for i in range(len(grades)):
        print(grades[i], '\t', end=' ')
    print()

print_menu()
menu_choice = 0
while menu_choice != 6:
    print()
    menu_choice = int(input("Menu Choice (1-6): "))
    if menu_choice == 1:
        name = input("Student to add: ")
        students[name] = [0] * len(max_points)
    elif menu_choice == 2:
        name = input("Students to remove: ")
        if name in students:
            del students[name]
        else:
            print("Student: ", name, "not found")
    elif menu_choice == 3:
        print_all_grades()
    elif menu_choice == 4:
        print("Record Grade")
        name = input("Student: ")
        if name in students:
            grades = students[name]
            print("Type in the number of the grade to record")
            print("Type a 0 (zero) to exit")
            for i in range(len(assignments)):
                print(i + 1, assignments[i], '\t', end=' ')
            print()
            print_grades(grades)
            which = 1234
            while which != -1:
                which = int(input("Change which Grade: "))
                which -= 1 #same as which = which - 1
                if 0 <= which < len(grades):
                    grade = int(input("Grade: "))
                    grades[which] = grade
                elif which != -1:
                    print("Invald Grade Number")
        else:
            print("Student not found")
    elif menu_choice != 6:
        print_menu()
