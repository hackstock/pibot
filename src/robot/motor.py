import RPi.GPIO as GPIO 

class PWMMotor(object):

    def __init__(self, name, forward_pin, backward_pin, pwm_freq=1000):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.name = name
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin

        GPIO.setup(self.forward_pin, GPIO.OUT)
        GPIO.setup(self.backward_pin, GPIO.OUT)

        self.forward_pwm = GPIO.PWM(self.forward_pin, pwm_freq)
        self.backward_pwm = GPIO.PWM(self.backward_pin, pwm_freq)

    def _move_forward(self, duty_cycle):
        self.backward_pwm.stop()
        self.forward_pwm.start(duty_cycle)

    def _move_backward(self, duty_cycle):
        self.forward_pwm.stop()
        self.backward_pwm.start(duty_cycle)

    def _clip_speed(self, speed):
        if speed < -100:
            return -100
        elif speed > 100:
            return 100
        else:
            return speed

    def move(self, speed):
        duty_cycle = abs(self._clip_speed(speed))
        if speed < 0:
            self._move_backward(duty_cycle)
        else:
            self._move_forward(duty_cycle)

    def stop(self):
        self.forward_pwm.stop()
        self.backward_pwm.stop()


