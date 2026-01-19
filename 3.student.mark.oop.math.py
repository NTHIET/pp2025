import math
import numpy as np

class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__id = student_id
        self.__name = student_name
        self.__dob = student_dob
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def __str__(self): return f"{self.__name} (ID:{self.__id}, DoB:{self.__dob})"

class Course:
    def __init__(self, course_id, course_name, course_credits):
        self.__id = course_id
        self.__name = course_name
        self.__credits = course_credits
    def get_id(self): return self.__id
    def get_credits(self): return self.__credits
    def __str__(self): return f"{self.__name} ({self.__id})"

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_data(self):
        for _ in range(int(input("Number of students: "))):
            self.students.append(Student(input("ID: "), input("Name: "), input("DoB: ")))
        for _ in range(int(input("Number of courses: "))):
            self.courses.append(Course(input("Course ID: "), input("Name: "), int(input("Credits: "))))

    def input_marks(self):
        for c in self.courses:
            for s in self.students:
                m = float(input(f"{s.get_name()} - {c}: "))
                self.marks[(c.get_id(), s.get_id())] = math.floor(m * 10) / 10

    def average_GPA(self):
        gpas = []
        for s in self.students:
            scores, credits = [], []
            for c in self.courses:
                k = (c.get_id(), s.get_id())
                if k in self.marks:
                    scores.append(self.marks[k])
                    credits.append(c.get_credits())
            gpa = np.average(scores, weights=credits) if scores else 0
            gpas.append((gpa, s))
        gpas.sort(key=lambda x: x[0], reverse=True)
        for g, s in gpas:
            print(s.get_name(), f"{g:.2f}")

    def list_students_curses(self):
        import curses
        def ui(stdscr):
            stdscr.addstr(0, 0, "STUDENT LIST")
            for i, s in enumerate(self.students, 2):
                stdscr.addstr(i, 0, str(s))
            stdscr.getch()
        curses.wrapper(ui)

    def run(self):
        self.input_data()
        while True:
            c = input("1.Input Marks\n2.GPA\n3.Curses\n4.Quit\nChoose option: ")
            if c == "1": self.input_marks()
            elif c == "2": self.average_GPA()
            elif c == "3": self.list_students_curses()
            else: break

if __name__ == "__main__":
    manager = MarkManager()
    manager.run()