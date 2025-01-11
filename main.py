from src.carcontroller import car_controller

if __name__ == "__main__":
    print("Hello RC Car World")
    car=car_controller()
    car.set_throttle(100)
    car.set_direction('left')
    