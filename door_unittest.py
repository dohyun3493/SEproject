import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback 

class TestExecuteCommandCallback(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car_controller = CarController(self.car)

    def test_open_door_when_vehicle_is_locked(self):
        self.car_controller.lock_vehicle()  # 차량 잠금
        execute_command_callback("LEFT_DOOR_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_status(), "CLOSED")

    def test_open_door_when_door_is_locked(self):
        self.car_controller.unlock_vehicle()  # 차량 잠금 해제
        self.car_controller.lock_left_door()  # 문 잠금
        execute_command_callback("LEFT_DOOR_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_status(), "CLOSED")

    def test_open_door_when_already_open(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.unlock_left_door()
        self.car_controller.open_left_door()  # 문이 이미 열린 상태
        execute_command_callback("LEFT_DOOR_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_status(), "OPEN")

    def test_open_door_successfully(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.unlock_left_door()
        self.car_controller.close_left_door()  # 문이 닫힌 상태
        execute_command_callback("LEFT_DOOR_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_status(), "OPEN")

if __name__ == "__main__":
    unittest.main()
