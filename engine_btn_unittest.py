import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

class test_engine_btn_successfully(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #차량이 잠겨 있지 않고 속도가 0일때 정상적으로 엔진이 켜지고 꺼지는지 확인하는 테스트
    def test_engine_btn_successfully(self): 
        #ENGINE_BTN동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        #ENGINE_BTN 호출
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , True)
        #ENGINE_BTN 호출
        execute_command_callback("ENGINE_BTN", self.car_controller)
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , False)

class test_engine_btn_when_vehicle_is_lock(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #차량이 잠겨 있을 때 엔진이 켜지지 않는 것을 확인하는 테스트
    def test_engine_btn_when_vehicle_is_lock(self): 
        #ENGINE_BTN동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        print(self.car_controller.get_engine_status())
        print(self.car_controller.get_lock_status())
        self.car_controller.lock_vehicle()
        print(self.car_controller.get_lock_status())
        #ENGINE_BTN 호출
        print(self.car_controller.get_engine_status())
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        print(self.car_controller.get_engine_status())
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , False)

class test_engine_btn_when_vehicle_has_speed(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #속도가 0이 아닐 때 엔진이 꺼지지 않는 것을 확인하는 테스트
    def test_engine_btn_when_vehicle_has_speed(self): 
        #ENGINE_BTN동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        self.car_controller.accelerate()
        #ENGINE_BTN 호출
        execute_command_callback("ENGINE_BTN", self.car_controller)
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , True)



if __name__ == "__main__":
    unittest.main(exit = False)