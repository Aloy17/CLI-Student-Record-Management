import json
from time import sleep

def search_student(students, field, value):

    found_students = []

    for student in students:

        if field == "ID":
            if student["ID"] == int(value):
                found_students.append(student)

        elif field == "Name":
            if student["Name"] == value.strip().upper():
                found_students.append(student)

    return found_students


def add_student(students):

    while True:
        student = {
                "ID" : 0,
                "Name" : "",
                "Age" : 0,
                "Course" : ""
                    }       

        student["ID"] = int(input("Student ID: ")) 
        student["Name"] = input("Student Name: ").strip().upper() 
        student["Age"] = int(input("Student Age: ")) 
        student["Course"] = input("Student Course: ").strip().upper()

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
            student_id = int(input("Enter ID: "))

            print(f"Listing Student with ID {student_id}")

            sleep(1)
            print(".")
            sleep(1)
            print(".")

            found_students = search_student(students, "ID", student_id)

            if found_students:
                for student in found_students:
                    print(student)
            else:
                print("No Match Found")


        case 2:
            student_name = input("Enter Name: ")
            print(f"Listing Student with Name '{student_name}'")
            sleep(1)
            print(".")
            sleep(1)
            print(".")

            found_students = search_student(students, "Name", student_name)
            
            if found_students:
                for student in found_students:
                    print(student)
            else:
                print("No Match Found")
            

        case 3:
            student_age = int(input("Enter Age: "))
            print(f"Listing Students with Age '{student_age}'")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            
            for student in students:
                if student["Age"] == student_age:
                    print(student)
                

        case 4:
            student_course = input("Enter Course: ")
            print(f"Listing Student with Course '{student_course}'")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            
            for student in students:
                if student["Course"] == student_course:
                    print(student)

        case 5:
            print("Listing All Students")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            
            for student in students:
                print(student)

        case _:
            print("Invalid Choice")


def update_student(students):
    print("""
    ========== UPDATE STUDENT ==========

    Find student using:

    [1] ID
    [2] Name
    """)

    choice = int(input("Choose a Number (1-2): "))

    match choice:
        case 1:
            choice = int(input("Enter ID: "))
            found_students = search_student(students,"ID",choice)

            if not found_students:
                print("ID Not Found")
                return


            
        case 2:
            student_name = input("Enter Name: ")
            found_students = search_student(students, "Name", student_name)

            if not found_students:
                print("Name Not Found")
                return

            
        case _:
            print("Invalid Choice")
            return


    if len(found_students) == 1:
        student = found_students[0]
        

    elif len(found_students) > 1:

        for i,student in enumerate(found_students, start=1):
            print(f"[{i}] {student}")

        choice = int(input("Which Student to Update? : "))

        student = found_students[choice - 1]



    print("""What would you like to edit?

        [1] Student Name

        [2] Student Age

        [3] Student Course
                """)

    choice = int(input("Type the NUMBER of the field you want to edit (1-3): "))

    match choice:
        case 1:
            ansr = input("Enter New Name: ")
            print(f"Changing Name from {student["Name"]} to {ansr}")

            choice = input("Continue? (Y/N)").strip().upper()
            if choice == "Y":
                student["Name"] = ansr
            else:
                return


        case 2:
            ansr = int(input("Enter New Age: "))
            print(f"Changing Name from {student["Age"]} to {ansr}")
        
            choice = input("Continue? (Y/N)").strip().upper()
            if choice == "Y":
                student["Age"] = ansr
            else:
                return


        case 3:
            ansr = input("Enter New Course: ")
            print(f"Changing Name from {student["Course"]} to {ansr}")
        
            choice = input("Continue? (Y/N)").strip().upper()
            if choice == "Y":
                student["Course"] = ansr
            else:
                return



def delete_student():
    pass

def load_student():
    with open("students.json", "r") as f:
        return json.load(f)

def save_student(students):
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)


students = load_student()

find_student(students)
