from services.motor_service import motor_service

class car_controller:
    def __init__(self):
        self.speed = 0
        self.direction = 'forward'
        self.motor_service = motor_service(2)
        
    def set_throttle(self, speed):
        if(speed < 0):
            print("Speed cannot be negative")
            return
        self.speed = speed
        print(f"Setting speed to {speed}")
        
    def set_direction(self, direction):
        if(direction in ['left', 'right', 'forward', 'backward']):
            self.direction = direction
        else:
            print(f"Invalid direction {direction}")

        print(f"Setting direction to {direction}")
        
    def get_throttle(self):
        return self.speed
        
    def get_direction(self):
        return self.direction
    
    def move(self):
        print(f"Moving {self.direction} at {self.speed}")
        if self.direction == 'forward':
            self.motor_service.activate_motors(self.speed, [0, 1])
        elif self.direction == 'backward':
            self.motor_service.activate_motors(-self.speed, [0, 1])
        elif self.direction == 'left':
            self.motor_service.activate_motors(self.speed, [0])
            self.motor_service.activate_motors(-self.speed, [1])
        elif self.direction == 'right':
            self.motor_service.activate_motors(-self.speed, [0])
            self.motor_service.activate_motors(self.speed, [1])

    def stop(self):
        print("Stopping")
