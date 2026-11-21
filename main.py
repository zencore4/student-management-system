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