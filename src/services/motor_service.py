"""
A service class to manage and control motors.
"""
class motor_service:

    """
    Initializes the motor_service with an empty dictionary of motors.
    """
    def __init__(self, motor_count):
        self.motors = {}
        for i in range(motor_count):
            self.motors[i] = motor(f"Motor {i}", i)

    """
    Activates the sp
    Args:
        momentum (flecified motors with the given momentum.
        oat): The momentum to apply to the motors.
        motors (list): A list of motor identifiers to be activated.
    """
    def activate_motors(self, momentum, motors):
        for motor in motors:
            if motor in self.motors:
                # This approach will leave a small window where 
                # the first motor activates before the second one.
                # To fix this, you can add a delay between the activations.
                # time.sleep(0.1) for example will delay it 1/10 of a second.
                # to do this we really need to have an inverted delay per motor 
                # activation (first motor 0.2, second motor .1, third motor 0.0)
                self.motors[motor].set_momentum(momentum)
                self.motors[motor].activate()
            else:
                print(f"Motor {motor} not found.")
    
    def deactivate_motors(self, motors):
        for motor in motors:
            if motor in self.motors:
                # Again we will want to delay the deactivation of the motors so 
                # they all stop at the same time.
                self.motors[motor].set_momentum(0)
                self.motors[motor].activate()
            else:
                print(f"Motor {motor} not found.")


class motor:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.momentum = 0

    def set_momentum(self, momentum):
        self.momentum = momentum

    def get_momentum(self):
        return self.momentum

    def activate(self):
        print(f"Activating motor {self.name} with momentum {self.momentum}")