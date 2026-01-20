import curses
def list_students_curses(students):
    def ui(stdscr):
        stdscr.addstr(0, 0, "STUDENT LIST")
        for i, s in enumerate(students, 2):
            stdscr.addstr(i, 0, str(s))
        stdscr.getch()
    curses.wrapper(ui)