import RPi.GPIO as GPIO 

from robot.motor import PWMMotor
from robot.utils import clip_speed

class PWMTank(object):

    def __init__(self, lm_fw_pin, lm_bw_pin, rm_fw_pin, rm_bw_pin):
        self.left_motor = PWMMotor(name="left_motor", forward_pin=lm_fw_pin, backward_pin=lm_bw_pin)
        self.right_motor = PWMMotor(name="right_motor", forward_pin=rm_fw_pin, backward_pin=rm_bw_pin)

    def move(self, speed):
        self.left_motor.move(speed)
        self.right_motor.move(speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def spin(self, lm_speed, rm_speed):
        lm_duty_cycle = clip_speed(lm_speed)
        rm_duty_cycle = clip_speed(rm_speed)

        self.left_motor.move(lm_duty_cycle)
        self.right_motor.move(rm_duty_cycle)
        

