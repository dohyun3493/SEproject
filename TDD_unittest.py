import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback


class TDDUnittest(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)
    
    # ENGINE_BTN 이후 브레이크 동시 입력된 경우
    def test_ENGINEBTN_BRAKE(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("ENGINE_BTN BRAKE", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , False) 
    
    # ENGINE_BTN만 입력된 경우
    def test_ENGINEBTN(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , False) 
    
    def testSet_five(self):
        self.car_controller.unlock_vehicle()
        
        execute_command_callback("LEFT_DOOR_OPEN ACCELERATE BRAKE RIGHT_DOOR_OPEN BRAKE ACCELERATE BRAKE BRAKE ENGINE_BIN",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_left_door_status(), "CLOSED")
        self.assertEqual(self.car_controller.get_right_door_status(), "CLOSED")
        self.assertEqual(self.car_controller.get_speed() , 0)

    def test_engine_brake(self):
        self.car_controller.unlock_vehicle()  # 차량 전체 잠금 해제
        self.car_controller.toggle_engine()  # 엔진 ON
        self.car_controller.brake() # 브레이크

        execute_command_callback("ENGINE_BIN BRAKE", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), False)

    def test_06(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() == True)
        
if __name__ == "__main__":
    unittest.main(exit = False)
    
