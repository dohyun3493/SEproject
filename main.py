import threading
from car import Car
from car_controller import CarController
from gui import CarSimulatorGUI

# execute_command를 제어하는 콜백 함수
# -> 이 함수에서 시그널을 입력받고 처리하는 로직을 구성하면, 알아서 GUI에 연동이 됩니다.

def execute_command_callback(command, car_controller):
    result = command.split()
    rts = False
    if len(result) != 1:
        if result[1] == "ENGINE_BTN" and result[0] == "BRAKE": 
            command = "ENGINE_BTN"
            rts = True
    print("check = ", rts)
    if command == "ENGINE_BTN":
        if rts == True:
            if car_controller.get_lock_status() == False: # 차량 잠금 상태가 해제되어 있는지 확인
                current_speed = car_controller.get_speed() # 현재 속도 확인
                if current_speed == 0:
                    car_controller.toggle_engine() # 시동 ON / OFF
        rts = False
    elif command == "ACCELERATE":
        if car_controller.get_lock_status() == False and car_controller.get_engine_status() == True :
            if car_controller.get_right_door_status() == "CLOSED" and car_controller.get_left_door_status() == "CLOSED":
                if car_controller.get_trunk_status() == True:    
                    if car_controller.get_speed() < 200 :
                        car_controller.accelerate()
            if car_controller.get_speed() >= 30:
                car_controller.lock_left_door()
                car_controller.lock_right_door()
    elif command == "BRAKE":
        if car_controller.get_speed() > 0:
            car_controller.brake()

    elif command == "LOCK":
        # 차량 잠금 조건 확인
        if car_controller.get_lock_status() == False:  # 차량이 잠겨 있지 않은 경우
            if car_controller.get_engine_status() == False:  # 엔진이 꺼져 있는 경우
                # 좌측 및 우측 도어 상태 확인
                if car_controller.get_left_door_status() == "OPEN":
                    car_controller.close_left_door() #왼쪽문 닫기
                    if car_controller.get_left_door_lock() == "UNLOCKED":
                        car_controller.lock_left_door()  # 왼쪽문 잠금
                else:
                    if car_controller.get_left_door_lock() == "UNLOCKED":
                        car_controller.lock_left_door()  # 왼쪽문 잠금
                    
                if car_controller.get_right_door_status() == "OPEN":
                    car_controller.close_right_door() #오른쪽문 닫기
                    if car_controller.get_right_door_lock() == "UNLOCKED":
                        car_controller.lock_right_door()  # 오른쪽문 잠금
                else:
                    if car_controller.get_right_door_lock() == "UNLOCKED":
                        car_controller.lock_right_door()  # 오른쪽문 잠금
                        
                # 트렁크 상태 확인
                if car_controller.get_trunk_status() == False:  # 트렁크가 열려 있는 경우
                    car_controller.close_trunk()  # 트렁크 닫기
                
                car_controller.lock_vehicle()  # 전체 잠금 장치 잠금
    elif command == "UNLOCK":
        # 차량 잠금 상태 확인
        if car_controller.get_lock_status() == True:  # 차량이 잠겨 있는 경우
            car_controller.unlock_vehicle()  # 차량 잠금 해제
        # 좌측 및 우측 도어가 모두 잠겨 있는지 확인
        if (car_controller.get_left_door_lock() == "LOCKED" or car_controller.get_right_door_lock() == "LOCKED"):
            car_controller.unlock_left_door() # 왼쪽 문 잠금 해제
            car_controller.unlock_right_door()  # 오른쪽 문 잠금 해제 
    elif command == "LEFT_DOOR_LOCK":
        if car_controller.get_lock_status() == False:
            if car_controller.get_left_door_status() == "CLOSED":
                if car_controller.get_left_door_lock() == "UNLOCKED":
                    car_controller.lock_left_door()  # 왼쪽 문 잠금
    elif command == "RIGHT_DOOR_LOCK":
        if car_controller.get_lock_status() == False:
            if car_controller.get_right_door_status() == "CLOSED":
                if car_controller.get_right_door_lock() == "UNLOCKED":
                    car_controller.lock_right_door()  # 오른쪽 문 잠금
    elif command == "LEFT_DOOR_UNLOCK":
        if car_controller.get_lock_status() == False:
            if car_controller.get_left_door_lock() == "LOCKED":
                if car_controller.get_speed() == 0:
                    car_controller.unlock_left_door()  # 왼쪽 문 잠금 해제
    elif command == "RIGHT_DOOR_UNLOCK":
        if car_controller.get_lock_status() == False:
            if car_controller.get_right_door_lock() == "LOCKED":
                if car_controller.get_speed() == 0:
                    car_controller.unlock_right_door()  # 오른쪽 문 잠금 해제
    elif command == "LEFT_DOOR_OPEN":
        if car_controller.get_lock_status() == False: 
            if car_controller.get_left_door_lock() == "UNLOCKED":
                if car_controller.get_left_door_status() == "CLOSED":
                    car_controller.open_left_door() 
    elif command == "RIGHT_DOOR_OPEN":
        if car_controller.get_lock_status() == False:
            if car_controller.get_right_door_lock() == "UNLOCKED": 
                if car_controller.get_right_door_status() == "CLOSED":
                    car_controller.open_right_door() 
    elif command == "LEFT_DOOR_CLOSE":
        if car_controller.get_left_door_status() == "OPEN":
            car_controller.close_left_door()
    elif command == "RIGHT_DOOR_CLOSE":
        if car_controller.get_right_door_status() == "OPEN":
            car_controller.close_right_door()
    elif command == "TRUNK_OPEN":
        if car_controller.get_lock_status() == False:
            if car_controller.get_trunk_status() == True:
                if car_controller.get_speed() == 0:
                    car_controller.open_trunk() # 트렁크 열기
    elif command == "TRUNK_CLOSE": 
        if car_controller.get_trunk_status() == False:
            car_controller.close_trunk() # 트렁크 닫기
    elif command == "SOS":
        if car_controller.get_speed() != 0:
            while car_controller.get_speed() != 0:
                car_controller.brake() # 차 정지
        car_controller.unlock_left_door() # 왼쪽 문 잠금 해제
        car_controller.unlock_right_door() # 오른쪽 문 잠금 해제
        car_controller.open_trunk() # 트렁크 열기
        
        
            

# 파일 경로를 입력받는 함수
# -> 가급적 수정하지 마세요.
#    테스트의 완전 자동화 등을 위한 추가 개선시에만 일부 수정이용하시면 됩니다. (성적 반영 X)
def file_input_thread(gui):
    while True:
        file_path = input("Please enter the command file path (or 'exit' to quit): ")

        if file_path.lower() == 'exit':
            print("Exiting program.")
            break

        # 파일 경로를 받은 후 GUI의 mainloop에서 실행할 수 있도록 큐에 넣음
        gui.window.after(0, lambda: gui.process_commands(file_path))

# 메인 실행
# -> 가급적 main login은 수정하지 마세요.
if __name__ == "__main__":
    car = Car()
    car_controller = CarController(car)

    # GUI는 메인 스레드에서 실행
    gui = CarSimulatorGUI(car_controller, lambda command: execute_command_callback(command, car_controller))

    # 파일 입력 스레드는 별도로 실행하여, GUI와 병행 처리
    input_thread = threading.Thread(target=file_input_thread, args=(gui,))
    input_thread.daemon = True  # 메인 스레드가 종료되면 서브 스레드도 종료되도록 설정
    input_thread.start()

    # GUI 시작 (메인 스레드에서 실행)
    gui.start()