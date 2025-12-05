class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__id = student_id
        self.__name = student_name
        self.__dob = student_dob

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def __str__(self):
        return f"{self.__name} (ID: {self.__id}, DoB: {self.__dob})"


class Course:
    def __init__(self, course_id, course_name):
        self.__id = course_id
        self.__name = course_name.strip()

    def get_id(self): return self.__id
    def get_name(self): return self.__name

    def __str__(self):
        return f"{self.__name} ({self.__id})"

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        
    def input_data(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            student_name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student_dob = input("Enter DoB (dd/mm/yyyy): ")
            self.students.append(Student(student_id, student_name, student_dob))
            
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))
            
    def input_marks(self):
        if not self.courses:
            print("No courses available. Please add courses first.")
            return
        if not self.students:
            print("No students available.")
            return

        print("SELECT A COURSE TO INPUT MARKS")
        for i, course in enumerate(self.courses, 1):
            print(f"{i}. {course}")

        try:
            choice = int(input("\nEnter course number: ")) - 1
            if not (0 <= choice < len(self.courses)):
                print("Invalid course number.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        selected_course = self.courses[choice]
        course_id = selected_course.get_id()
        course_name = selected_course.get_name()

        print(f"ENTERING MARKS FOR COURSE: {course_name} ({course_id})")
        print("-" * 10)

        for student in self.students:
            while True:
                try:
                    mark = float(input(f"  Mark for {student.get_name()} (ID {student.get_id()}): "))
                    if 0 <= mark <= 20:
                        self.marks[(course_id, student.get_id())] = mark
                        break
                    else:
                        print("   → Mark must be between 0 and 20!")
                except ValueError:
                    print("   → Please enter a valid number!")
    def list_courses(self):
        print("LIST OF COURSES")
        if not self.courses:
            print("No courses available.")
        for c in self.courses:
            print(f"- {c}")

    def list_students(self):
        print("LIST OF STUDENTS")
        if not self.students:
            print("No students available.")
        for s in self.students:
            print(f"- {s}")

    def show_marks_for_course(self):
        if not self.courses:
            print("No courses available.")
            return
        
        print("\nSelect a course to show marks:")
        for i, course in enumerate(self.courses, 1):
            print(f"{i}. {course}")

        try:
            choice = int(input("\nEnter course number: ")) - 1
            if not (0 <= choice < len(self.courses)):
                print("Invalid course number.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return
        
        selected_course = self.courses[choice]
        course_id = selected_course.get_id()
        print(f"\nMarks for course: {course.get_name()}")
        print("-" * 3)

        found = False
        for student in self.students:
            key = (course_id, student.get_id())
            if key in self.marks:
                mark = self.marks[key]
                print(f"{student.get_name()} (ID {student.get_id()}): {mark}/20")
                found = True
        
        if not found:
            print("No marks entered for this course yet.")

    def run(self):
        print("=== Student Mark Management System ===")
        self.input_data()
        
        while True:
            print("\n" + "="*40)
            print("1. Input marks for a course")
            print("2. List courses")
            print("3. List students")
            print("4. Show students marks for a course")
            print("5. QUIT")
            print("="*40)
            
            choice = input("Select an option (1-5): ")
            if choice == '1':
                self.input_marks()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_marks_for_course()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please select a number between 1 and 5.")

if __name__ == "__main__":
    manager = MarkManager()
    manager.run()