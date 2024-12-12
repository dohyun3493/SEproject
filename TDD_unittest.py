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

    # 브레이크 후 엑셀 밟고 엔진 입력된 경우
    def test_brake_accel_engine(self):
        self.car_controller.unlock_vehicle()  # 차량 잠금 해제

        execute_command_callback("BRAKE ACCELERATE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), False)

    def test_06(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() == True)

    #브레이크 이후 동시 입력으로 엔진 외에 다른 장치의 입력이 들어왔을 때 testcase
    def test_brake_no_engine_everyone(self):
         #ENGINE_BTN동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        #브레이크 및 엔진외 다른 장치 동시 호출
        execute_command_callback("BRAKE ACCELERTE", self.car_controller)
        #BRAKE ACCELERATE동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_speed(), 0)
        
if __name__ == "__main__":
    unittest.main(exit = False)
    
