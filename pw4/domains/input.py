from domains.students import Student
from domains.courses import Course

def input_data(mark_manager):
    for _ in range(int(input("Number of students: "))):
        mark_manager.students.append(Student(input("ID: "), input("Name: "), input("DoB: ")))
    for _ in range(int(input("Number of courses: "))):
        mark_manager.courses.append(Course(input("Course ID: "), input("Name: "), int(input("Credits: "))))