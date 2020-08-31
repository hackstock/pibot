from robot_base import PWMTank
import curses

class DifferentialDriveTank(object):

    def __init__(self, rm_fw_pin=9, rm_bw_pin=10, lm_fw_pin=8, lm_bw_pin=7):
        self.tank = PWMTank(
            rm_fw_pin=rm_fw_pin,
            rm_bw_pin=rm_bw_pin,
            lm_fw_pin=lm_fw_pin,
            lm_bw_pin=lm_bw_pin
        )

    def move(self, speed):
        self.tank.move(speed)

    def spin(self, lm_speed, rm_speed):
        self.tank.spin(lm_speed, rm_speed)

    def stop(self):
        self.tank.stop()

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
            tank.spin(50,-50)
        elif key == curses.KEY_ENTER  or key in [10,13]:
            tank.stop()


if __name__ == "__main__":
    curses.wrapper(main)