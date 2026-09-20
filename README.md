# Student Record Management System (CLI)

## Project Description

A menu driven console application written in Python for managing student records. It allows a user to add, view, search, update and delete records, and stores them in a JSON file so that data is retained after the program is closed.



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

<img width="597" height="328" alt="Screenshot 2026-09-20 at 10 18 46 PM" src="https://github.com/user-attachments/assets/46953997-94d7-4621-a456-5bc031ba630a" />



**Adding a student**


<img width="543" height="209" alt="Screenshot 2026-09-20 at 10 19 18 PM" src="https://github.com/user-attachments/assets/ea22ec8d-cc21-454e-a624-6e9817528459" />



**Invalid input during Add**

<img width="511" height="220" alt="Screenshot 2026-09-20 at 10 20 15 PM" src="https://github.com/user-attachments/assets/2e11caf3-1c6d-4460-b963-a0b7bce8cf2e" />



**Viewing all students**

<img width="571" height="406" alt="Screenshot 2026-09-20 at 10 21 45 PM" src="https://github.com/user-attachments/assets/db63bf79-5bd9-48e2-95f6-c8d3d680c182" />



**Search by ID**

<img width="530" height="317" alt="Screenshot 2026-09-20 at 10 22 20 PM" src="https://github.com/user-attachments/assets/c6d6b329-5040-49fc-83b6-c7cb4d2f92af" />



**Search by name**

<img width="543" height="319" alt="Screenshot 2026-09-20 at 10 22 51 PM" src="https://github.com/user-attachments/assets/a3842f07-00f0-477b-9613-f01b3a53f5c0" />




**Updating a student**

<img width="455" height="426" alt="Screenshot 2026-09-20 at 10 23 32 PM" src="https://github.com/user-attachments/assets/a3f51d48-2b34-4e17-8f9b-fe9163e13811" />



**Deleting a student**

<img width="507" height="216" alt="Screenshot 2026-09-20 at 10 23 59 PM" src="https://github.com/user-attachments/assets/7dfb1d15-a8b8-4561-9bf6-a6fb1f108eab" />



**Invalid menu choices**

<img width="515" height="303" alt="Screenshot 2026-09-20 at 10 24 17 PM" src="https://github.com/user-attachments/assets/1cbbddf9-faed-4eef-8ee2-3582c88e3d5e" />



**Data stored in students.json**

<img width="275" height="462" alt="Screenshot 2026-09-20 at 10 24 40 PM" src="https://github.com/user-attachments/assets/06ec0685-dddb-462d-8dd1-740efcba1571" />


**Missing data file handled**

<img width="1434" height="538" alt="image" src="https://github.com/user-attachments/assets/a2fd95c1-9be0-4096-b8e4-3d7176767d80" />





