import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

# 테스트 케이스 1) 엔진 꺼진 상태에서 브레이크 후 엔진 동시 입력된 경우 
class TDDUnittest01(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    def testSet_01(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , True)

# 테스트케이스 2) 엔진 꺼진 상태에서 엔진 후 브레이크 동시 입력된 경우
class TDDUnittest02(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    def testSet_02(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("ENGINE_BTN BRAKE", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , False) 

# 테스트케이스 3) 엔진 꺼진 상태에서 엔진만 입력된 경우
class TDDUnittest03(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    def testSet_03(self):
        self.car_controller.unlock_vehicle()
        execute_command_callback("ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status() , False) 

# 테스트케이스 4) 한 줄에 BRAKE ENGINE_BTN의 전후관계 만족시 시동이 켜지고 나머지 다른 동작들이 각 조건에 맞게 동작하는지 확인하는 테스트
class TDDUnittest040(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #시동키기 이전 동작 확인
    def testSet_040(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.unlock_left_door()  
        execute_command_callback("LEFT_DOOR_OPEN BRAKE ENGINE_BTN",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_left_door_status(), "OPEN")

class TDDUnittest041(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #시동키기 이후 동작 확인
    def testSet_041(self):
        self.car_controller.unlock_vehicle()     
        self.car_controller.unlock_left_door()  
        execute_command_callback("BRAKE ENGINE_BTN LEFT_DOOR_OPEN",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_left_door_status(), "OPEN")

class TDDUnittest042(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    #BRAKE와 ENGINE_BTN 사이 동작 확인
    def testSet_042(self):
        self.car_controller.unlock_vehicle() 
        self.car_controller.unlock_left_door()  
        execute_command_callback("BRAKE LEFT_DOOR_OPEN ENGINE_BTN",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_left_door_status(), "OPEN")

class TDDUnittest043(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    # ACCELERATE과 BRAKE ENGINE_BTN
    def testSet_043(self):
        self.car_controller.unlock_vehicle()  
        self.car_controller.unlock_left_door()  
        execute_command_callback("BRAKE ENGINE_BTN ACCELERATE",self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_speed() , 0)

# 테스트케이스 5) 엔진 켜진 상태에서 브레이크 후 엔진 동시 입력된 경우
class TDDUnittest050(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    def testSet_050(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), False)

class TDDUnittest051(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    def testSet_051(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        self.car_controller.accelerate()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), False)

class TDDUnittest052(unittest.TestCase):
    car = Car()
    car_controller = CarController(car)

    def testSet_052(self):
        self.car_controller.unlock_vehicle()
        self.car_controller.toggle_engine()
        self.car_controller.accelerate()
        self.car_controller.accelerate()
        execute_command_callback("BRAKE ENGINE_BTN", self.car_controller)
        self.assertEqual(self.car_controller.get_engine_status(), True)
        self.assertEqual(self.car_controller.get_speed() , 10)
 
if __name__ == "__main__":
    unittest.main(exit = False)
