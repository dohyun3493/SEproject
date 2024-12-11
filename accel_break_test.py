import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

class Test_Accel_Braek(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)
    
    # 액셀 테스트
    def testAccel(self):
        #★★ 주의!! 엑셀과 브레이크에 대한 태스트만을 포함하고 있음!! ★★
        #★★ 다른 기능은 제약조건에 맞게 구현되어 있지 않음!!! ★★
        
        # 전체잠금장치 해제, 엔진 on 상태, 
        self.car_controller.toggle_engine()
        self.car_controller.unlock_vehicle()

        # car 클래스가 초기화할때 트렁크, 문, 은 전부 닫혀있고, 양쪽 문은 잠겨있음.
        # 액셀을 밟았을때 현재 속도가 0 에서 10만큼 증가 하였나?
        execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 10)
        
        # 문이 열려있을때 엑셀이 작동을 안하는가?
        self.car_controller.open_left_door()
        execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 10)
        self.car_controller.close_left_door() # 테스트 후 원래 상태로 복귀
        
        # 트렁크가 열려있을때 엑셀이 작동을 안하는가?
        self.car_controller.open_trunk()
        execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 10)
        self.car_controller.close_trunk() # 테스트 후 원래 상태로 복귀
        
        # 속도가 200 이상일때 엑셀이 작동을 안하는가?
        for i in range(0,20): # 10 + 200 조건에 의하여 200까지 밖에 안올라야함.
            execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 200)
        for i in range(0,21): # 브레이크를 21번 작동시켜 속도를 0으로 만듦
            execute_command_callback("BRAKE",self.car_controller)
        
        # 엔진이 꺼져있을때 엑셀이 작동을 안하는가?
        self.car_controller.toggle_engine() # 엔진 off
        execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 0)
        self.car_controller.toggle_engine() # 다시 엔진을 on 시킴
        
        # 전체잠금장치가 LOCK이라면 엑셀이 작동을 안하는가?
        self.car_controller.lock_vehicle() # 잠금장치 on
        execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 0)
        self.car_controller.unlock_vehicle() # 잠금장치 of 시킴
        
        # 속도가 30이상일때 엑셀을 밟으면 문의 잠금장치가 자동으로 잠기는가?
        self.car_controller.unlock_left_door()
        self.car_controller.unlock_right_door() # 양쪽문 잠금 해제
        for i in range(0,2): # 속도를 0에서 20까지 올림
            execute_command_callback("ACCELERATE",self.car_controller)
        # 현재 문잠금이 unlock 상태인가?
        self.assertEqual(self.car_controller.get_left_door_lock(),"UNLOCKED") 
        self.assertEqual(self.car_controller.get_right_door_lock(),"UNLOCKED") 
        execute_command_callback("ACCELERATE",self.car_controller) # 속도를 20에서 30을 올림
        # 액셀을 밟은후 현재 문잠금이 lock 상태인가?
        self.assertEqual(self.car_controller.get_left_door_lock(),"LOCKED") 
        self.assertEqual(self.car_controller.get_right_door_lock(),"LOCKED") 
        for i in range(0,3): # 속도를 0으로
            execute_command_callback("BRAKE",self.car_controller) 
            
    # 브레이크 테스트  
    def testBraek(self):
    
        # 브레이크가 제대로 동작하는가?
        execute_command_callback("ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 10)
        execute_command_callback("BRAKE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 0)
        
        # 속도가 0이하일때 동작하지 않는가?
        execute_command_callback("BRAKE",self.car_controller)
        self.assertEqual(self.car_controller.get_speed(), 0)

if __name__ == "__main__":
    unittest.main(exit = False)