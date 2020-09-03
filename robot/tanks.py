from robot.robot_base import PWMTank

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

