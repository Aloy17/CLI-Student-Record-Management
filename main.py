import student_operations as st

def main():
    print("""
    ╔══════════════════════════════════════════╗
    ║       STUDENT RECORD MANAGEMENT          ║
    ╠══════════════════════════════════════════╣
    ║                                          ║
    ║   [1]  Add Student                       ║
    ║   [2]  View Students                     ║
    ║   [3]  Update Student                    ║
    ║   [4]  Delete Student                    ║
    ║                                          ║
    ║   [Q]  Quit                              ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """)

    students = st.load_student()
    if students is None:
        print("Unable to start the application because the student data file is missing.")
        return

    while True:

        choice = input("Enter your choice [1-4] OR Q").strip().upper()

        match choice:
            case "1":
                st.add_student(students)

            case "2":
                st.find_student(students)

            case "3":
                st.update_student(students)

            case "4":
                st.delete_student(students)

            case "Q":
                break

            case _:
                print("Invalid Entry")


if __name__ == "__main__":
    main()

    