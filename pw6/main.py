from domains.mark_manager import MarkManager
from input import input_data
from storage import save, load

def main():
    mark_manager = load()

    if mark_manager is None:
        mark_manager = MarkManager()
        input_data(mark_manager)

    while True:
        n = input("1.Input Marks\n2.GPA\n3.List Students\n4.List Courses\n5.Quit\nChoose option: ")
        if n == "1":
            mark_manager.input_marks()
        elif n == "2":
            mark_manager.average_GPA()
        elif n == "3":
            from output import list_students_curses
            list_students_curses(mark_manager.students)
        elif n == "4":
            from output import list_courses_curses
            list_courses_curses(mark_manager.courses)
        else:
            save(mark_manager)
            break

if __name__ == "__main__":
    main()