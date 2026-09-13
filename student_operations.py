import json
from time import sleep

def add_student(students):

    while True:
        student = {
                "ID" : 0,
                "Name" : "",
                "Age" : 0,
                "Course" : ""
                    }       

        student["ID"] = int(input("Student ID: ")) 
        student["Name"] = input("Student Name: ") 
        student["Age"] = int(input("Student Age: ")) 
        student["Course"] = input("Student Course: ") 

        print("Student Details Entered")
        print(student)

        ansr = input("Continue? (Y/N): ").strip().upper()

        if ansr == "Y":
            students.append(student)
            print("Student Details Added")
        else:
            student.clear()
            print("All details cleared")

        next = input ("Add Another Student? (Y/N): ").strip().upper()
        if next != "Y":
            break

    

def find_student(students):
    print("""
    ========== VIEW STUDENTS ==========

    Choose how you want to view student records.

    [1] View one student by ID
    [2] View one student by Name
    [3] View students by Age
    [4] View students by Course
    [5] View all students
    """)
    choice = int(input("Type the NUMBER of your choice (1-5): "))

    match choice:
        case 1:
            student_id = int(input("Enter ID"))
            print(f"Listing Student with ID {student_id}")
            sleep(1)
            print(".")
            sleep(1)
            print(".")

            for student in students:
                if student["ID"] == student_id:
                    print(student)



        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case _:
            print("Invalid Choice")


def update_student():
    pass

def delete_student():
    pass

def load_student():
    with open("students.json", "r") as f:
        return json.load(f)

def save_student(students):
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

