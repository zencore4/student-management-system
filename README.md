# student-management-system
A simple console-based Student Management System in Python built using Object-Oriented Programming concepts.


# Student Management System

A menu-driven console application built in **Python** using **Object-Oriented Programming (OOP)**. It lets you add students, view all students, and search for a student by roll number.

## Features

- Add a new student (name, roll number, age, course)
- Display all students
- Search a student by roll number
- Simple menu-based interface
- Basic handling of empty records and "student not found" cases

## OOP Concepts Used

- **Classes and Objects**: `Student` and `Dashboard` classes
- **Constructor (`__init__`)**: to initialize student data and the student list
- **Encapsulation**: student data and related operations are grouped inside classes
- **Methods**: `display_details()`, `add_student()`, `show_all()`, `search_student()`

## Project Structure

| Class | Responsibility |
|-------|----------------|
| `Student` | Stores a student's details and displays them |
| `Dashboard` | Manages the list of students (add, show, search) |

## How to Run

1. Make sure Python 3 is installed
2. Clone the repository:
