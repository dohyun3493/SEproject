import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback


class TDDUnittest(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)
    
    # 테스트케이스 1) 엔진 후 브레이크 동시 입력된 경우
    def testSet_01(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("ENGINE_BTN BRAKE", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , False) 
    
    # 테스트케이스 2) 엔진만 입력된 경우
    def testSet_02(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , False) 
    
    # 테스트케이스 3) 다수의 입력 후 엔진 동시 입력된 경우
    def testSet_03(self):
        self.car_controller.unlock_vehicle()        
        execute_command_callback("LEFT_DOOR_OPEN ACCELERATE BRAKE RIGHT_DOOR_OPEN BRAKE ACCELERATE BRAKE BRAKE ENGINE_BIN",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_left_door_status(), "CLOSED")
        self.assertEqual(self.car_controller.get_right_door_status(), "CLOSED")
        self.assertEqual(self.car_controller.get_speed() , 0)

    # 테스트케이스 4) 브레이크 후 엑셀 밟고 엔진 동시 입력된 경우
    def testSet_04(self):
        self.car_controller.unlock_vehicle()  # 차량 잠금 해제
        execute_command_callback("BRAKE ACCELERATE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), False)
        
    # 테스트케이스 5) 브레이크 후 엔진 동시 입력된 경우
    def testSet_05(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)

    # 테스트케이스 6) 브레이크 이후 동시 입력으로 엔진 외에 다른 장치의 입력이 들어왔을 때 testcase
    def testSet_06(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        execute_command_callback("BRAKE ACCELERTE", self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 0)
        
if __name__ == "__main__":
    unittest.main(exit = False)
    
