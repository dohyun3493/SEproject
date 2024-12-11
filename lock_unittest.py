import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

class TestCarsos(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #차량이 잠겨 있지 않고, 엔진이 꺼져 있으며, 양쪽 문이 닫힘 및 잠겨 있고, 트렁크가 닫혀 있다면 차량 잠금을 하는 것을 확인하는 테스트
    def test_lock_successfully(self): 
        #LOCK동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        #LOCK 호출
        execute_command_callback("LOCK", self.car_controller)
        #LOCK 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_lock_status() , True) 

    #차량이 잠겨 있지 않고, 엔진이 꺼져 있으며, 양쪽 문이 열려 있고, 트렁크가 열려 있다면 문을 닫고 잠금한 후 트렁크를 닫고 차량 잠금을 하는 것을 확인하는 테스트
    def test_lock_when__open_both_door_and_trunk(self): 
        #LOCK동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        self.car_controller.unlock_left_door()
        self.car_controller.unlock_right_door()
        self.car_controller.open_left_door()
        self.car_controller.open_right_door()
        self.car_controller.open_trunk()
        #LOCK 호출
        execute_command_callback("LOCK", self.car_controller)
        #LOCK 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_lock_status() , True)  
        self.assertEqual(self.car_controller.get_left_door_lock() , "LOCKED") 
        self.assertEqual(self.car_controller.get_right_door_lock() , "LOCKED") 
        self.assertEqual(self.car_controller.get_trunk_status() , True)

if __name__ == "__main__":
    unittest.main(exit = False)