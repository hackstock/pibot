from motor import PWMMotor

class PWMTank(object):

    def __init__(self, lm_pin_one, lm_pin_two, rm_pin_one, rm_pin_two):
        self.left_motor = PWMMotor(name="left_motor", pin_one=lm_pin_one, pin_two=lm_pin_two)
        self.right_motor = PWMMotor(name="right_motor", pin_one=rm_pin_one, pin_two=rm_pin_two)

    def move(self, speed):
        self.left_motor.move(speed)
        self.right_motor.move(speed)
        