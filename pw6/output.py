import curses
def list_students_curses(students):
    def ui(stdscr):
        stdscr.addstr(0, 0, "STUDENT LIST")
        for i, s in enumerate(students, 2):
            stdscr.addstr(i, 0, str(s))
        stdscr.getch()
    curses.wrapper(ui)
    
def list_courses_curses(courses):
    def ui(stdscr):
        stdscr.addstr(0, 0, "COURSE LIST")
        for i, c in enumerate(courses, start=2):
            stdscr.addstr(
                i, 0,
                f"ID: {c.get_id()}, Name: {c}, Credits: {c.get_credits()}"
            )
        stdscr.getch()
    curses.wrapper(ui)