

# Course Management System

A modular **Course Management System built with Python OOPs** that demonstrates core Object-Oriented Programming concepts along with custom exception handling, centralized logging, and a professional Git/GitHub development workflow.

The application uses a **menu-driven command-line interface (CLI)**, allowing users to create students, mentors, courses, assign courses, and enroll students at runtime.

---

## Project Overview

The Course Management System manages:

* Students
* Mentors
* Courses
* Student enrollments
* Mentor-course assignments

The project is designed to demonstrate how Python OOP concepts can be combined with modular application development practices.

### Key concepts demonstrated

* Abstraction
* Inheritance
* Encapsulation
* Polymorphism
* Instance methods
* `@staticmethod`
* `@classmethod`
* Custom exception handling
* Centralized logging
* Properties
* Modular coding
* Git feature branches
* Meaningful commits
* Pull Requests
* Branch merging

---

# Project Structure

```text
course_management_system/
│
├── main.py
├── user.py
├── student.py
├── mentor.py
├── course.py
├── enrollment.py
├── exception.py
├── logging_config.py
├── README.md
├── .gitignore
└── course_management.log
```

> `course_management.log` is generated automatically when the application runs and is excluded from Git using `.gitignore`.

---

# Architecture

The application follows a modular architecture where each class has a specific responsibility.

```text
                         User
                    Abstract Base Class
                       /          \
                      /            \
                 Student          Mentor
                    |                |
                    |                |
                    +-------+--------+
                            |
                          Course
                            |
                       Enrollment
```

---

# Module Description

| Module              | Responsibility                       |
| ------------------- | ------------------------------------ |
| `main.py`           | Menu-driven CLI and user interaction |
| `user.py`           | Abstract `User` base class           |
| `student.py`        | Student functionality                |
| `mentor.py`         | Mentor functionality                 |
| `course.py`         | Course management                    |
| `enrollment.py`     | Student-course enrollment            |
| `exception.py`      | Custom application exceptions        |
| `logging_config.py` | Centralized logging configuration    |
| `.gitignore`        | Excludes generated/unnecessary files |
| `README.md`         | Project documentation                |

---

# Classes

## 1. User

`User` is an abstract base class.

It contains common properties shared by students and mentors:

* User ID
* Name
* Email

It defines abstract methods:

```python
get_role()
display_profile()
```

It also contains a static method for email validation:

```python
validate_email()
```

### OOP concepts

* Abstraction
* Encapsulation
* Static method
* Abstract methods

---

## 2. Student

`Student` inherits from `User`.

```python
class Student(User):
```

### Responsibilities

* Store student information
* Maintain enrolled courses
* Enroll in courses
* Display student profile

### Methods

```python
enroll()
get_courses()
display_profile()
create_student()
```

The class method:

```python
Student.create_student()
```

acts as an alternative constructor.

---

## 3. Mentor

`Mentor` also inherits from `User`.

```python
class Mentor(User):
```

### Responsibilities

* Store mentor information
* Store specialization
* Manage assigned courses
* Display mentor profile

### Methods

```python
add_course()
get_courses()
display_profile()
create_mentor()
```

---

## 4. Course

The `Course` class manages course information and enrolled students.

### Responsibilities

* Store course information
* Generate course IDs
* Maintain enrolled students
* Display course information
* Track total courses

### Important methods

```python
add_student()
get_students()
display_course()
generate_course_id()
create_course()
```

The class demonstrates both:

```python
@staticmethod
```

and:

```python
@classmethod
```

---

## 5. Enrollment

The `Enrollment` class represents the relationship between a student and a course.

### Responsibilities

* Create an enrollment
* Enroll a student into a course
* Store enrollment date
* Display enrollment information

Example:

```python
enrollment = Enrollment(
    student,
    course
)

enrollment.enroll_student()
```

---

# Object-Oriented Programming Concepts

## Abstraction

The `User` class is an abstract base class.

```python
from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_role(self):
        pass
```

The subclasses must implement the abstract methods.

---

## Inheritance

Both `Student` and `Mentor` inherit from `User`.

```python
class Student(User):
```

```python
class Mentor(User):
```

This avoids duplication of common user functionality.

---

## Encapsulation

Internal data is protected using private attributes.

For example:

```python
self.__email
self.__courses
self.__students
```

Properties are used to provide controlled access to the data.

---

## Polymorphism

Both `Student` and `Mentor` implement:

```python
get_role()
```

but return different values.

```python
for user in users:
    print(user.get_role())
```

Possible output:

```text
Student
Mentor
```

The same method call behaves differently depending on the object.

---

## Instance Methods

Instance methods operate on individual objects.

Examples:

```python
student.enroll(course)
```

```python
mentor.add_course(course)
```

```python
course.display_course()
```

---

## Static Method

The `Course` class contains a static method for generating course IDs.

```python
Course.generate_course_id("Python OOP")
```

The method does not require an instance of `Course`.

---

## Class Method

Class methods are used as alternative constructors.

For example:

```python
Student.create_student(
    user_id,
    name,
    email
)
```

and:

```python
Course.create_course(
    title,
    description
)
```

---

# Exception Handling

Custom exceptions are maintained separately in:

```text
exception.py
```

The project contains exceptions such as:

```python
CourseManagementException
InvalidEmailException
DuplicateCourseException
CourseNotFoundException
EnrollmentException
UserNotFoundException
```

This keeps error handling separate from the application's business logic.

Example:

```python
try:
    student.enroll(course)

except EnrollmentException as error:
    print(f"Enrollment failed: {error}")
```

---

# Logging

Logging is centralized in:

```text
logging_config.py
```

The application records important events including:

* User creation
* Student creation
* Mentor creation
* Course creation
* Course assignment
* Student enrollment
* Validation errors
* Enrollment errors
* Unexpected application errors

Logs are written to:

```text
course_management.log
```

Example log:

```text
2026-09-28 20:10:01 - INFO - student - Student created: Avro
2026-09-28 20:10:15 - INFO - course - Course created: Python OOP
2026-09-28 20:10:30 - INFO - enrollment - Enrollment successful
```

The log file is excluded from version control through `.gitignore`.

---

# Installation

## Prerequisites

Make sure Python is installed.

Check the Python version:

```bash
python --version
```

Python 3.10+ is recommended.

---

## Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project:

```bash
cd course_management_system
```

---

## Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Dependencies

The project uses only Python standard-library modules.

No external packages are required.

The main standard-library modules used include:

```text
abc
logging
datetime
```

---

# Running the Application

Run:

```bash
python main.py
```

The application starts with a menu:

```text
=======================================================
        COURSE MANAGEMENT SYSTEM
=======================================================

1. Create Student
2. Create Mentor
3. Create Course
4. Assign Course to Mentor
5. Enroll Student in Course
6. Display Student
7. Display Mentor
8. Display Course
9. Demonstrate Polymorphism
10. Display System Statistics
0. Exit

Enter your choice:
```

---

# Application Usage

## 1. Create Student

Select:

```text
1
```

The application asks for:

```text
Enter student ID:
Enter student name:
Enter student email:
```

Example:

```text
Enter student ID: STU001
Enter student name: Avro
Enter student email: avro@gmail.com
```

The student is created at runtime.

---

## 2. Create Mentor

Select:

```text
2
```

The application asks for:

```text
Enter mentor ID:
Enter mentor name:
Enter mentor email:
Enter specialization:
```

Example:

```text
Enter mentor ID: MEN001
Enter mentor name: Rahul
Enter mentor email: rahul@gmail.com
Enter specialization: Python Development
```

---

## 3. Create Course

Select:

```text
3
```

The application asks for:

```text
Enter course title:
Enter course description:
```

Example:

```text
Enter course title: Python OOP
Enter course description: Learn Object Oriented Programming with Python
```

The course ID is generated automatically.

---

## 4. Assign Course to Mentor

Select:

```text
4
```

The currently created course is assigned to the currently created mentor.

Example:

```text
Course 'Python OOP' assigned to mentor 'Rahul'.
```

---

## 5. Enroll Student

Select:

```text
5
```

The current student is enrolled in the current course.

The system creates an `Enrollment` object and records the enrollment date.

---

## 6. Display Student

Select:

```text
6
```

The system displays:

```text
--- Student Profile ---

ID      : STU001
Name    : Avro
Email   : avro@gmail.com
Courses : 1

Enrolled Courses:
- CRS-PYTHON-OOP: Python OOP
```

---

## 7. Display Mentor

Select:

```text
7
```

The mentor profile and assigned courses are displayed.

---

## 8. Display Course

Select:

```text
8
```

The course details and enrolled students are displayed.

---

## 9. Demonstrate Polymorphism

Select:

```text
9
```

The application demonstrates polymorphism by treating students and mentors as `User` objects.

Example:

```text
========== Polymorphism ==========

Avro -> Student
Rahul -> Mentor
```

---

## 10. Display System Statistics

Select:

```text
10
```

The system displays:

```text
========== System Statistics ==========

Total Courses: 1
Total Enrollments: 1
```

---

# Error Handling Examples

## Invalid Email

If the user enters:

```text
Enter student email: abc
```

the application raises:

```text
InvalidEmailException
```

and displays an appropriate error message.

---

## Duplicate Enrollment

If a student attempts to enroll in the same course again, the application raises:

```text
EnrollmentException
```

instead of allowing duplicate enrollment.

---

# Git & GitHub Workflow

The project is developed using Git feature branches rather than implementing everything directly on `main`.

## Initial Repository

```bash
git init
```

```bash
git add .
```

```bash
git commit -m "Initialize course management system"
```

---

# Feature Branches

Suggested branch structure:

```text
main
│
├── feature/user-management
├── feature/course-management
├── feature/enrollment
├── feature/logging-exception
└── feature/documentation
```

---

## Feature 1 — User Management

Create the branch:

```bash
git checkout -b feature/user-management
```

Implement:

```text
user.py
student.py
mentor.py
```

Commit:

```bash
git add .
git commit -m "Add user abstraction student and mentor classes"
```

Push:

```bash
git push -u origin feature/user-management
```

Create a Pull Request on GitHub and merge it into `main`.

---

## Feature 2 — Course Management

```bash
git checkout main
git pull

git checkout -b feature/course-management
```

Implement:

```text
course.py
```

Commit:

```bash
git add .
git commit -m "Add course management functionality"
```

Push:

```bash
git push -u origin feature/course-management
```

Create a Pull Request and merge it into `main`.

---

## Feature 3 — Enrollment

```bash
git checkout main
git pull

git checkout -b feature/enrollment
```

Implement:

```text
enrollment.py
```

Commit:

```bash
git add .
git commit -m "Add student course enrollment functionality"
```

Push:

```bash
git push -u origin feature/enrollment
```

Create a Pull Request and merge it into `main`.

---

## Feature 4 — Logging and Exceptions

```bash
git checkout main
git pull

git checkout -b feature/logging-exception
```

Implement:

```text
logging_config.py
exception.py
```

Integrate logging and exception handling into the application.

Commit:

```bash
git add .
git commit -m "Add centralized logging and exception handling"
```

Push:

```bash
git push -u origin feature/logging-exception
```

Create a Pull Request and merge it into `main`.

---

## Feature 5 — Documentation

```bash
git checkout main
git pull

git checkout -b feature/documentation
```

Add and update:

```text
README.md
```

Commit:

```bash
git add README.md
git commit -m "Add project documentation and usage guide"
```

Push:

```bash
git push -u origin feature/documentation
```

Create a Pull Request and merge it into `main`.

---

# Expected Git History

A possible final history:

```text
main

* Add project documentation and usage guide
* Add centralized logging and exception handling
* Add student course enrollment functionality
* Add course management functionality
* Add user abstraction student and mentor classes
* Initialize course management system
```

You can inspect the history using:

```bash
git log --oneline --graph --all
```

---

# GitHub Pull Request Workflow

Each feature should follow:

```text
Create Feature Branch
        ↓
Implement Feature
        ↓
Test Feature
        ↓
Commit Changes
        ↓
Push Feature Branch
        ↓
Create Pull Request
        ↓
Review Changes
        ↓
Merge PR
        ↓
Update Local Main
```

This simulates a real software development workflow.

---

# Features

* Menu-driven CLI
* Runtime user input
* Student management
* Mentor management
* Course management
* Course assignment
* Student enrollment
* Enrollment tracking
* Course ID generation
* Email validation
* Custom exceptions
* Centralized logging
* OOP architecture
* Abstract classes
* Inheritance
* Encapsulation
* Polymorphism
* Static methods
* Class methods
* Git feature branches
* Pull Request workflow

---

# Future Enhancements

The current version is intentionally focused on demonstrating Python OOP and Git concepts.

Potential future improvements include:

### Database Integration

Replace in-memory objects with:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

### Additional Features

* Multiple students
* Multiple mentors
* Multiple courses
* Search students by ID
* Search courses by ID
* Remove students
* Remove courses
* Course completion tracking
* Course ratings
* Authentication
* Student dashboard
* Mentor dashboard
* REST APIs
* Unit testing with `pytest`

---

# Learning Outcomes

After completing this project, the developer should be able to demonstrate practical understanding of:

```text
Python OOP
    ↓
Classes & Objects
    ↓
Inheritance
    ↓
Encapsulation
    ↓
Abstraction
    ↓
Polymorphism
    ↓
Static & Class Methods
    ↓
Exception Handling
    ↓
Logging
    ↓
Modular Architecture
    ↓
Git Branching
    ↓
Pull Requests
    ↓
GitHub Collaboration
```

---

# Author

Developed as a Python Object-Oriented Programming project to demonstrate modular application development, exception handling, logging, and professional Git/GitHub workflow.
