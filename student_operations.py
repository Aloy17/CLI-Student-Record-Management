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


#If a duplicate ID is entered it'll still be accepted
def add_student(students): 

    while True:
        student = {
                "ID" : 0,
                "Name" : "",
                "Age" : 0,
                "Course" : ""
                    } 
        while True:     
            try:
                student["ID"] = int(input("Enter Student ID: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.") 
            
        student["Name"] = input("Enter Student Name: ").strip().upper() 

        while True:
            try:
                student["Age"] = int(input("Enter Student Age: ")) 
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            
        student["Course"] = input("Enter Student Course: ").strip().upper()

        print("Student details entered:")
        print(student)

        ansr = input("Confirm adding this student? (Y/N): ").strip().upper()

        if ansr == "Y":
            students.append(student)
            save_student(students)
            print("Student added successfully.")

        next = input ("Add another student? (Y/N): ").strip().upper()
        if next != "Y":
            break
    

def find_student(students): #Exception Handling for ensuring user types correct data type
    print("""
    ========== VIEW STUDENT RECORDS ==========

    Select a search option:

    [1] View one student by ID
    [2] View one student by Name
    [3] View students by Age
    [4] View students by Course
    [5] View all students
    """)

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
            
        if not 1 <= choice <=5:
            print("Invalid choice. Please enter a number from 1 to 5.")
        else:
            break

    match choice:

        case 1:
            while True:
                try:
                    student_id = int(input("Enter Student ID: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

                print(f"Searching for student with ID: {student_id}")

                sleep(1)
                print(".")
                sleep(1)
                print(".")

                found_students = search_student(students, "ID", student_id)

                if found_students:
                    for student in found_students:
                        print(student)
                else:
                    print("No matching student records found.")


        case 2:
            student_name = input("Enter Student Name: ")
            print(f"Searching for students with name: '{student_name}'")
            sleep(1)
            print(".")
            sleep(1)
            print(".")

            found_students = search_student(students, "Name", student_name)
            
            if found_students:
                for student in found_students:
                    print(student)
            else:
                print("No matching student records found.")
            

        case 3:
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    
            print(f"Searching for students with age: {student_age}")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            
            for student in students:
                if student["Age"] == student_age:
                    print(student)
                

        case 4:
            student_course = input("Enter Student Course: ").strip().upper()
            print(f"Searching for students enrolled in: {student_course}")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            
            for student in students:
                if student["Course"] == student_course:
                    print(student)

        case 5:
            print("Displaying all student records:")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            
            for student in students:
                print(student)

        case _:
            print("Invalid Choice")


def update_student(students): #Exception Handling for ensuring user types correct data type while finding and while changing
    print("""
    ========== UPDATE STUDENT RECORD ==========

    Select how you want to find the student:

    [1] ID
    [2] Name
    """)

    while True:
        try:
            choice = int(input("Enter your choice (1-2): "))
            if not 1<= choice <= 2:
                print("Invalid choice. Please enter 1 or 2.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")



    match choice:
        case 1:
            while True:
                try:
                    choice = int(input("Enter Student ID: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            found_students = search_student(students,"ID",choice)
            if not found_students:
                print("No student found with the specified ID.")
                return


            
        case 2:
            student_name = input("Enter Student Name: ").strip().upper()
            found_students = search_student(students, "Name", student_name)

            if not found_students:
                print("No student found with the specified name.")
                return

            
        case _:
            print("Invalid Choice")
            return


    if len(found_students) == 1:
        student = found_students[0]
        

    elif len(found_students) > 1:

        for i,student in enumerate(found_students, start=1):
            print(f"[{i}] {student}")

        while True:
            try:
                choice = int(input("Select the student you want to update: "))
                if not 1<= choice <= len(found_students):
                    print("Invalid selection. Please choose a number from the list above.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        student = found_students[choice - 1]



    print("""Select the field you want to update:

        [1] Student Name

        [2] Student Age

        [3] Student Course
                """)

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if not 1<= choice <= 3:
                print("Invalid choice. Please enter a number from 1 to 3.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    match choice:
        case 1:
            ansr = input("Enter New Student Name: ").strip().upper()
            print(f"Changing Name from {student["Name"]} to {ansr}.")

            choice = input("Confirm this change? (Y/N):").strip().upper()
            if choice == "Y":
                student["Name"] = ansr
            else:
                return


        case 2:
            while True:
                try:
                    ansr = int(input("Enter New Student Age: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            print(f"Changing Age from {student["Age"]} to {ansr}.")
        
            choice = input("Confirm this change? (Y/N):").strip().upper()
            if choice == "Y":
                student["Age"] = ansr
            else:
                return


        case 3:
            ansr = input("Enter New Student Course: ").strip().upper()
            print(f"Changing Course from {student["Course"]} to {ansr}.")
        
            choice = input("Confirm this change? (Y/N):").strip().upper()
            if choice == "Y":
                student["Course"] = ansr
            else:
                return
    save_student(students)


def delete_student(students):
    print("""
        ========== DELETE STUDENT RECORD ==========
    
        Select how you want to find the student:
    
        [1] ID
        [2] Name
        """)

    while True:
        try:
            choice = int(input("Enter your choice (1-2): "))
            if not 1<= choice <= 2:
                print("Invalid choice. Please enter 1 or 2.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    match choice:
        case 1:
            while True:
                try:
                    choice = int(input("Enter Student ID: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            found_students = search_student(students,"ID",choice)

            if not found_students:
                print("No matching student record found.")
            else:
                students.remove(found_students[0])
                save_student(students)


        case 2:
            choice = input("Enter Student Name: ").strip().upper()
            found_students = search_student(students,"Name",choice)

            if not found_students:
                print("No matching student record found.")
            else:
                for i,student in enumerate(found_students, start=1):
                    print(f"[{i}] {student}")

                while True:
                    try:
                        choice = int(input("Select the student you want to delete: "))
                        if not 1<= choice <= len(found_students):
                            print("Invalid selection. Please choose a number from the list above.")
                        else:
                            break

                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                student = found_students[choice - 1]

            students.remove(student)
            save_student(students)

def load_student():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Student data file not found. Starting with an empty student list.")
        return []

def save_student(students): 
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
        
   
        


