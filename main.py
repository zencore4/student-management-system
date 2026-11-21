class Student:
    def __init__(self, name, roll_no, age, course):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Age:", self.age)
        print("Course:", self.course)


class Dashboard:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all(self):
        for student in self.students:
            student.display_details()
            print()

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None


db = Dashboard()          

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll_no = int(input("Enter roll number: "))
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        s1 = Student(name, roll_no, age, course)
        db.add_student(s1)
        print("Student added.")

    elif choice == "2":
        if len(db.students) == 0:
            print("No students yet.")
        else:
            db.show_all()

    elif choice == "3":
        roll_no = int(input("Enter roll number to search: "))
        found = db.search_student(roll_no)
        if found:
            found.display_details()
        else:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
