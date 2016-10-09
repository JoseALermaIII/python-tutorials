#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~
# Now modify the grades program from section Dictionaries so that it uses
# file I/O to keep a record of the students.

assignments = ['hw ch 1', 'hw ch 2', 'quiz     ', 'hw ch 3', 'test']
students = { }

def load_grades(gradesfile):
    inputfile = open(gradesfile, "r")
    grades = [ ]
    while True:
        student_and_grade = inputfile.readline()
        student_and_grade = student_and_grade[:-1]
        if not student_and_grade:
            break
        else:
            studentname, studentgrades = student_and_grade.split(",")
            studentgrades = studentgrades.split(" ")
            students[studentname] = studentgrades
    inputfile.close()
    print("Grades loaded.")

def save_grades(gradesfile):
    outputfile = open(gradesfile, "w")
    for k, v in students.items():
        outputfile.write(k + ",")
        for x in v:
            outputfile.write(str(x) + " ")
        outputfile.write("\n")
    outputfile.close()
    print("Grades saved.")

def print_menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Load grades")
    print("4. Record grade")
    print("5. Print grades")
    print("6. Save grades")
    print("7. Print Menu")
    print("9. Quit")

def print_all_grades():
    if students:
        keys = sorted(students.keys())
        print('\t', end=' ')
        for x in assignments:
            print(x, '\t', end=' ')
        print()
        for x in keys:
            print(x, '\t', end=' ')
            grades = students[x]
            print_grades(grades)
    else:
        print("There are no grades to print.")

def print_grades(grades):
    for x in grades:
        print(x, '\t', end=' ')
    print()

print_menu()
menu_choice = 0
while menu_choice != 9:
    print()
    menu_choice = int(input("Menu Choice: "))
    if menu_choice == 1:
        name = input("Student to add: ")
        students[name] = [0] * len(assignments)
    elif menu_choice == 2:
        name = input("Student to remove: ")
        if name in students:
            del students[name]
        else:
            print("Student:", name, "not found")
    elif menu_choice == 3:
        gradesfile = input("Load grades from which file? ")
        load_grades(gradesfile)
    elif menu_choice == 4:
        print("Record Grade")
        name = input("Student: ")
        if name in students:
            grades = students[name]
            print("Type in the number of the grade to record")
            print("Type a 0 (zero) to exit")
            for i,x in enumerate(assignments):
                print(i + 1, x, '\t', end=' ')
            print()
            print_grades(grades)
            which = 1234
            while which != -1:
                which = int(input("Change which Grade: "))
                which -= 1
                if 0 <= which < len(grades):
                    grade = input("Grade: ") # Change from float(input()) to input() to avoid an error when savi
                    grades[which] = grade
                elif which != -1:
                    print("Invalid Grade Number")
        else:
            print("Student not found")
    elif menu_choice == 5:
        print_all_grades()
    elif menu_choice == 6:
        gradesfile = input("Save grades to which file? ")
        save_grades(gradesfile)
    elif menu_choice != 9:
        print_menu()
