import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback


class TDDUnittest(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car_controller = CarController(self.car)
    

if __name__ == "__main__":
    unittest.main(exit = False)
    