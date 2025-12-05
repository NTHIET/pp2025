students = []
courses = []
marks = {}

def input_data():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        student_dob = input("Enter DoB (dd/mm/yyyy): ")
        students.append((student_id, student_name, student_dob))
        
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
        
    print("\nSelect a course to input marks: ")
    for i, (course_id, course_name) in enumerate(courses):
        print(f"{i + 1}. {course_name} ({course_id})")
            
    choice = int(input("Enter course number: ")) - 1
    if choice < 0 or choice >= len(courses):
        print("Invalid course number.")
        return

    selected_course_id = courses[choice][0]
    print(f"\n>>> Entering marks for course: {courses[choice][1]}")
    
    for student_id, student_name, student_dob in students:
        while True:
            try:
                mark = float(input(f"   Mark for {student_name} (ID {student_id}): "))
                if 0 <= mark <= 20:
                    marks[(selected_course_id, student_id)] = mark
                    break
                else:
                    print(">>    Mark must be 0-20!")
            except ValueError:
                print("   Please enter a number!")

def list_courses():
    print("\nCourses:")
    if not courses:
        print("No courses available.")
        return
    for course_id, course_name in courses:
        print(f"- {course_id}: {course_name}")

def list_students():
    print("\nStudents:")
    if not students:
        print("No students available.")
        return
    for student_id, student_name, student_dob in students:
        print(f"- {student_id}: {student_name}, DoB: {student_dob}")

def show_marks_for_course():
    if not courses:
        print("No courses available.")
        return
    
    print("\nSelect a course to show marks:")
    for i, (course_id, course_name) in enumerate(courses):
        print(f"{i + 1}. {course_name} ({course_id})")

    choice = int(input("Enter course number: ")) - 1
    if choice < 0 or choice >= len(courses):
        print("Invalid course number.")
        return
    
    selected_course_id = courses[choice][0]
    print(f"\nMarks for course: {courses[choice][1]}")
    print("-" * 3)
    
    found = False
    for student_id, student_name, student_dob in students:
        key = (selected_course_id, student_id)
        if key in marks:
            print(f"{student_name} (ID {student_id}): {marks[key]}")
            found = True
        else:
            print(f"{student_name} (ID {student_id}): no mark")
    if not found:
        print("No marks available for this course.")

def main():
    print("=== Student Mark Management System ===")
    input_data()
    
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
            print("\n>>> Input Marks for a Course")
            for i, (course_id, course_name) in enumerate(courses):
                print(f"{i + 1}. {course_name} ({course_id})")
            course_choice = int(input("Enter course number: ")) - 1
            if 0 <= course_choice < len(courses):
                course_id = courses[course_choice][0]
                course_name = courses[course_choice][1]
                print(f"\n>>> Entering marks for: {course_name}")
                for (student_id, student_name) in students:
                    while True:
                        try:
                            marks = float(input(f"   Mark for {student_name} (ID {student_id}): "))
                            if 0 <= marks <= 20:
                                marks[(course_id, student_id)] = marks
                                break
                            else:
                                print("    Mark must be 0 - 20!")
                        except ValueError:
                            print("   Please enter a number!")
            else:
                print("Invalid course number.")
        
        elif choice == '2':
            list_courses()
        elif choice == '3':
            list_students()
        elif choice == '4':
            show_marks_for_course()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()