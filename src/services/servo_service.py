import RPi.GPIO as GPIO
import time
import logging

class servo_service:
    default_duty_cycle = 2.5
    def __init__(self, servo_pin=17):
        """
        Initializes the Servo class.
        
        Args:
            servo_pin (int, optional): The GPIO pin number to which the servo is connected. Defaults to 18.
        """
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.NullHandler())
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)  # 25 Hz (40 ms period)
        self.pwm.start(self.default_duty_cycle)  # Duty cycle of 2.5% for 0 degrees
        time.sleep(1)
        
        self.log.info("Servo service configured successfully")
        
        
    def rotate(self, angle):
        """
        Rotates the servo to the desired angle.
        
        Args:
            angle (float): The desired angle in degrees (0 to 180).
        """

        # Add model logic here and alter behavior between different units
        #if angle < 25:
        #    self.log.warn("Requested angle was too small, increased to 25.")
        #    angle = 25

        duty_cycle = self.default_duty_cycle + (angle / 18.0)  # Calculate duty cycle for the desired angle
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)
        
    def reset(self):
        """
        Resets the servo to the zero-degree position.
        """
        self.log.info("Resetting servo.")
        self.rotate(20)
        
    def cleanup(self):
        """
        Stops the PWM and cleans up the GPIO.
        """
        self.log.info("Servo service is executing cleanup routine.")
        self.pwm.stop()
        GPIO.cleanup()
