from domains.students import Student
from domains.courses import Course

def input_data(mark_manager):
    for _ in range(int(input("Number of students: "))):
        mark_manager.students.append(Student(input("ID: "), input("Name: "), input("DoB: ")))
        
    for _ in range(int(input("Number of courses: "))):
        mark_manager.courses.append(Course(input("Course ID: "), input("Name: "), int(input("Credits: "))))
        
    load_data(mark_manager)

def load_data(mark_manager):
    with open("students.txt", "w") as f:
            for s in mark_manager.students:
                f.write(f"ID: {s.get_id()}, Name: {s.get_name()}, DoB: {s.get_dob()}\n")
                
    with open("courses.txt", "w") as f:
            for c in mark_manager.courses:
                f.write(f"ID: {c.get_id()}, Name: {c}, Credits: {c.get_credits()}\n")