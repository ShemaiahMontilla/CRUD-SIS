# Student Information System
"""
elements :- ['id-number', 'name','course', 'year-level', 'gender', ]
1. Add New Student
2. Display list of students
3. Search a student by id number
4. Edit student
5. Delete a Student
6. Quit
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import csv
# Define global variables
student_elements = [ 'id_number','name', 'course ','year_level', 'gender ', ]
student_database = 'students.csv'

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Information System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. Display list of students")
    print("3. Search a student by id number")
    print("4. Edit student")
    print("5. Delete a Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_elements
    global student_database

    # [ ['1','2'] ]
    student_data = []
    for elements in student_elements:
        value = input("Enter " + elements + ": ")
        student_data.append(value)

    with open(student_database, "a",
     encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def display_students():
    global student_elements
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_elements
    global student_database

    print("--- Search Student ---")
    id_number = input("Enter id-number. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if id_number == row[0]:
                    print("----- Student Found -----")
                    print("ID-Number: ", row[0])
                    print("Name: ", row[1])
                    print("Course: ", row[2])
                    print("Year-Level: ", row[3])
                    print("Gender: ", row[4])
                    
                    break
        else:
            print("ID-Number. not found in our database")
    input("Press any key to continue")


def edit_student():
    global student_elements
    global student_database

    print("--- Update Student ---")
    id_number = input("Enter id-number to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_number == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for elements in student_elements:
                        value = input("Enter " + elements + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID-Number not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_elements
    global student_database

    print("--- Delete Student ---")
    id_number = input("Enter id-number. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_number != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID-Number. ", id_number, "deleted successfully")
    else:
        print("ID-Number not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        edit_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")