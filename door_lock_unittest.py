import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

# 문 잠금 유닛테스트
class Testdoorlock(unittest.TestCase):
    def setUp(self):
        self.car = Car()  # Car 인스턴스 생성
        self.car_controller = CarController(self.car)

    # 모든 제약조건을 만족할 때 왼쪽 문 잠금
    def test_lock_left_door_when_all(self):
        self.car_controller.unlock_vehicle() # 차량 전체 잠금 해제
        self.car_controller.unlock_left_door() # 왼쪽 문 잠금 해제
        self.car_controller.close_left_door() # 왼쪽 문 닫기
        # 왼쪽 문 잠금 시도
        execute_command_callback("LEFT_DOOR_LOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "LOCKED")

    # 전체 잠금 상태에서 왼쪽 문 잠금 시도 --> 실패(UNLOCKED)
    def test_lock_left_door_when_lock_vehicle(self):
        self.car_controller.lock_vehicle() # 차량 전체 잠금
        self.car_controller.unlock_left_door() # 왼쪽 문 잠금 해제
        # 왼쪽 문 잠금 시도
        execute_command_callback("LEFT_DOOR_LOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")

    # 이미 잠긴 왼쪽 문 잠금 --> 실패(LOCKED)
    def test_lock_left_door_when_lock_left_door(self):
        self.car_controller.unlock_vehicle() # 차량 전체 잠금 해제
        self.car_controller.lock_left_door() # 왼쪽 문 잠금
        # 왼쪽 문 잠금 시도
        execute_command_callback("LEFT_DOOR_LOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "LOCKED")

    # 왼쪽 문이 열려 있는 상태에서 왼쪽 문 잠금 --> 실패(UNLOCKED)
    def test_lock_left_door_when_open_left_door(self):
        self.car_controller.unlock_vehicle() # 차량 전체 잠금 해제
        self.car_controller.unlock_left_door() # 왼쪽 문 잠금 해제
        self.car_controller.open_left_door() # 왼쪽 문 열기
        # 왼쪽 문 잠금 시도
        execute_command_callback("LEFT_DOOR_LOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")

# 문 잠금 해제 유닛테스트
class TestDoorUnlock(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car_controller = CarController(self.car)

    # 모든 요구사항이 충족되었을 때 왼쪽 문 잠금 해제
    def test_lock_left_door_when_all(self):
        self.car_controller.unlock_vehicle() # 차량 전체 잠금 해제
        self.car_controller.lock_left_door() # 왼쪽 문 잠금
        self.car_controller.car__speed = 0 # 차량 속도 0으로
        # 왼쪽 문 잠금 해제 시도
        execute_command_callback("LEFT_DOOR_UNLOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")

    # 전체 잠금 상태에서 왼쪽 문 잠금 해제 --> 실패(LOCKED)
    def test_unlock_vehicle_when_lock_vehicle(self):
        self.car_controller.lock_vehicle() # 차량 전체 잠금
        # 왼쪽 문 잠금 해제 시도
        execute_command_callback("LEFT_DOOR_UNLOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "LOCKED")

    # 이미 잠금 해제된 왼쪽 문 잠금 해제 --> 실패(UNLOCKED)
    def test_unlock_left_door_when_unlock_left_door(self):
        self.car_controller.unlock_vehicle() # 차량 전체 잠금 해제
        self.car_controller.unlock_left_door() # 왼쪽 문 잠금 해제
        # 왼쪽 문 잠금 해제 시도
        execute_command_callback("LEFT_DOOR_UNLOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")

    # 자동차 속도가 0 이상일 때 왼쪽 문 잠금 해제 --> 실패(LOCKED)
    def test_unlock_left_door_when_accelerate(self):
        self.car_controller.unlock_vehicle() # 차량 전체 잠금 해제
        self.car_controller.toggle_engine() # 엔진 ON
        self.car_controller.accelerate() # 엑셀
        # 왼쪽 문 잠금 해제 시도
        execute_command_callback("LEFT_DOOR_UNLOCK", self.car_controller)
        self.assertEqual(self.car_controller.get_left_door_lock(), "LOCKED")

if __name__ == "__main__":
    unittest.main(exit=False)
