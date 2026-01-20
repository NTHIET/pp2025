from domains.mark_manager import MarkManager
from input import input_data
from output import list_students_curses
def main():
    manager = MarkManager()
    input_data(manager)
    
    while True:
        n = input("1.Input Marks\n2.GPA\n3.Curses\n4.Quit\nChoose option: ")
        if n == "1":
            manager.input_marks()
        elif n == "2":
            manager.average_GPA()
        elif n == "3":
            list_students_curses(manager.students)
        else:
            break

if __name__ == "__main__":
    main()