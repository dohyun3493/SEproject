import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback


class TDDUnittest(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)
        
    
    def testSet_five(self):
        self.car_controller.unlock_vehicle()
        
        execute_command_callback("LEFT_DOOR_OPEN ACCELERATE BRAKE RIGHT_DOOR_OPEN BRAKE ACCELERATE BRAKE BRAKE ENGIN_BIN",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_left_door_status(), "CLOSED")
        self.assertEqual(self.car_controller.get_right_door_status(), "CLOSED")
        self.assertEqual(self.car_controller.get_speed() , 0)


if __name__ == "__main__":
    unittest.main(exit = False)
    