import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

#트렁크 유닛테스트   
class TestTrunkState(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car_controller = CarController(self.car)
       
    #트렁크 open 시 전체 잠금장치가 잠긴 경우    
    def test_open_trunk_when_vehicle_is_locked(self):
        self.car_controller.lock_vehicle()
        execute_command_callback("TRUNK_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_trunk_status(), True)
        
    #트렁크 open 시 차량의 속도가 0이 아닌 경우 -> 전체 잠금 장치는 열림
    def test_open_trunk_when_vehicle_has_speed(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        self.car_controller.accelerate()
        execute_command_callback("TRUNK_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_trunk_status(), True)
        
    #트렁크 open 시 모든 제약조건을 만족할 때
    def test_open_trunk_successfully(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("TRUNK_OPEN", self.car_controller)
        self.assertEqual(self.car_controller.get_trunk_status(), False)
        
    #트렁크 close
    def test_close_trunk_successfully(self):
        execute_command_callback("TRUNK_CLOSE", self.car_controller)
        self.assertEqual(self.car_controller.get_trunk_status(), True)

if __name__ == "__main__":
    unittest.main(exit = False)
    

#코드 -> 설명
    











