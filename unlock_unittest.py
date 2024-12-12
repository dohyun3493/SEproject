import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

class TestUnlockState(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    # 차량이 잠겨 있을 때 차량 잠금 해제 및 양쪽 문 잠금 해제를 하는것을 확인하는 테스트 
    def test_unlock_successfully(self):
        #UNLOCK 호출
        execute_command_callback("UNLOCK", self.car_controller)
        #UNLOCK 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_lock_status() , False)
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")
        self.assertEqual(self.car_controller.get_right_door_lock(), "UNLOCKED")

    #차량이 잠겨 있지 않을 때 차량이 잠금 해제된 상태를 유지 및 양쪽 문 잠금 해제를 하는것을 확인하는 테스트
    def test_unlock_when_vehicle_already_unlock(self):
        #UNLOCK동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        #UNLOCK 호출
        execute_command_callback("UNLOCK", self.car_controller)
        #UNLOCK 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_lock_status() , False) 
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")
        self.assertEqual(self.car_controller.get_right_door_lock(), "UNLOCKED")

if __name__ == "__main__":
    unittest.main(exit = False)