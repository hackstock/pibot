import RPi.GPIO as GPIO 

class PWMMotor(object):

    def __init__(self, name, pin_one, pin_two, pwm_freq=1000):

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two

        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)

        self.pwm_one = GPIO.PWM(self.pin_one, pwm_freq)
        self.pwm_two = GPIO.PWM(self.pin_two, pwm_freq)

    def _move_forward(self, duty_cycle):
        self.pwm_two.stop()
        self.pwm_one.start(duty_cycle)

    def _move_backward(self, duty_cycle):
        self.pwm_one.stop()
        self.pwm_two.start(duty_cycle)

    def move(self, speed):
        duty_cycle = abs(speed)
        if speed < 0:
            self._move_backward(duty_cycle)
        else:
            self._move_forward(duty_cycle)

    def stop(self):
        self.pwm_one.stop()
        self.pwm_two.stop()


