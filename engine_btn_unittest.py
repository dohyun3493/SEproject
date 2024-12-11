import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

class TestCarsos(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)
    
    #차량이 잠겨 있지 않고 속도가 0일때 정상적으로 엔진이 켜지고 꺼지는지 확인하는 테스트
    def test_engine_btn_successfully(self): 
        #ENGINE_BTN동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.unlock_vehicle()
        #ENGINE_BTN 호출
        execute_command_callback("ENGINE_BTN", self.car_controller)
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , True)  
        #ENGINE_BTN 호출
        execute_command_callback("ENGINE_BTN", self.car_controller)
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , False) 

    #차량이 잠겨 있을 때 엔진이 켜지지 않는 것을 확인하는 테스트
    def test_engine_btn_when_vehicle_is_lock(self): 
        #ENGINE_BTN동작이 작동되는지 확인하기 위해 차량의 상태를 업데이트
        self.car_controller.lock_vehicle()
        #ENGINE_BTN 호출
        execute_command_callback("ENGINE_BTN", self.car_controller)
        #ENGINE_BTN 동작 이후 테스트 진행
        self.assertEqual(self.car_controller.get_engine_status() , False)

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