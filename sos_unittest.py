import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

#SOS 유닛테스트
class TestCarsos(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car_controller = CarController(self.car)
    
    def test_sos(self):
        #SOS동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.toggle_engine()
        self.car_controller.open_left_door()
        self.car_controller.open_right_door()
        self.car_controller.close_trunk()
        self.car_controller.accelerate()
            
        #SOS 호출
        execute_command_callback("SOS", self.car_controller)
        
        #SOS 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_speed(), 0)
        self.assertEqual(self.car_controller.get_left_door_lock(), "UNLOCKED")
        self.assertEqual(self.car_controller.get_right_door_lock(), "UNLOCKED")
        self.assertEqual(self.car_controller.get_trunk_status(), False)
     
if __name__ == "__main__":
    unittest.main(exit = False)
    
    
