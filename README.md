# Student Record Management System (CLI)

## Project Description

A menu driven console application written in Python for managing student records. It allows a user to add, view, search, update and delete records, and stores them in a JSON file so that data is retained after the program is closed.

This project was developed as Assignment 1 (Mini Project) for Python Programming and Relational Database, MCA Semester I.

## Features

* Menu driven interface with a main menu and sub menus, and Q to quit
* Add a student (ID, Name, Age, Course) with a confirmation step, and add several students in one session
* View or search students by ID, Name, Age or Course, or list all records
* Update a student's Name, Age or Course, located by ID or Name
* Delete a student located by ID or Name
* Duplicate name handling: matching students are listed and the user selects the required record
* Validation of every numeric entry and menu choice, with clear error messages and repeated prompts
* Automatic saving to `students.json` after every add, update and delete
* Missing file handling: if `students.json` does not exist, the program starts with an empty list and creates the file on the first save

## Technologies and Concepts Used

* Python 3.12 or higher (the code uses the `match` statement)
* Standard library modules: `json` for file storage and `time` for a short delay during searches
* Data types and variables: `int`, `str`, `list` and `dict`
* Conditional statements and loops
* Functions and modular design across two files
* Exception handling with `ValueError` and `FileNotFoundError`, together with range validation
* File I/O using JSON
* Git and GitHub for version control

## Project Structure

```
main.py                 Entry point and main menu loop
student_operations.py   Record management functions
students.json           Data file for persistent storage
screenshots/            Screenshots of the working application
README.md               Project documentation
```

Each student is stored as a dictionary inside a list:

```python
{"ID": 101, "Name": "RYANE", "Age": 24, "Course": "MCA"}
```

Names and courses are stored in uppercase, so searching by name or course does not depend on how the text is typed.

## How to Run

1. Install Python 3.12 or higher.
2. Clone the repository and open the project folder:

```
git clone https://github.com/Aloy17/CLI-Student-Record-Management.git
cd CLI-Student-Record-Management
```

3. Start the application:

```
python main.py
```

On macOS and Linux, use `python3` instead of `python`. Run the program from inside the project folder, because `students.json` is read from the current working directory.

## Sample Input and Output

Adding a student:

```
Enter Student ID: 104
Enter Student Name: zed
Enter Student Age: 22
Enter Student Course: mca
Student details entered:
{'ID': 104, 'Name': 'ZED', 'Age': 22, 'Course': 'MCA'}
Confirm adding this student? (Y/N): Y
Student added successfully.
```

Searching by name:

```
Enter Student Name: zed
Searching for students with name: 'zed'
.
.
{'ID': 104, 'Name': 'ZED', 'Age': 22, 'Course': 'MCA'}
```

Handling invalid input:

```
Enter Student ID: abc
Invalid input. Please enter a valid number.
Enter Student ID: 105
```

## Screenshots

**Main menu**

![Main menu](screenshots/01_main_menu.png)

**Adding a student**

![Adding a student](screenshots/02_add_student.png)

**Invalid input during Add**

![Invalid input](screenshots/03_invalid_input.png)

**Viewing all students**

![Viewing all students](screenshots/04_view_all.png)

**Search by ID**

![Search by ID](screenshots/05_search_by_id.png)

**Search by name**

![Search by name](screenshots/06_search_by_name.png)

**Updating a student**

![Updating a student](screenshots/07_update_student.png)

**Deleting a student**

![Deleting a student](screenshots/08_delete_student.png)

**Invalid menu choices**

![Invalid menu choices](screenshots/09_invalid_menu.png)

**Data stored in students.json**

![students.json](screenshots/10_json_persistence.png)

**Missing data file handled**

![Missing data file](screenshots/11_file_not_found.png)



