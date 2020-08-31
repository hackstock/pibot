import curses

import DifferentialDriveTank

def main(stdscr):
    curses.curs_set(0)
    tank = DifferentialDriveTank()

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            tank.move(50)
        elif key == curses.KEY_DOWN:
            tank.move(-50)
        elif key == curses.KEY_LEFT:
            tank.spin(-50,50)
        elif key == curses.KEY_RIGHT:
            tank.spin(-50,50)
        elif key == curses.KEY_ENTER  or key in [10,13]:
            tank.stop()


if __name__ == "__main__":
    curses.wrapper(main)
