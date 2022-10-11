import time
from pynput.mouse import Listener
import pyautogui
from datetime import datetime
import keyboard
from PIL import ImageGrab


#새로고침 초
start_time = 59
#새로고침 위치
click_xy=[87,49]


#1. 방지 클릭 : Enter
click_1=[1183,360]
#2. 보안문자 입력 이동
click_2=[542,495]
#3. 보안문자 완료
click_3=[538,550]
#4.구역 이동 및 클릭
click_4=[790,297]
#5. 좌석이동
click_5=[280,635]
#6. 좌석예매완료
click_6=[794,622]
#비어있는 좌석 색상
chk_color = [[124,104,238],[28,168,20],[23,179,255],[251,126,78],[251,126,79]]


def start() :
	now = datetime.now()
	chk_time=0
	while chk_time==0:
		current_time = now.strftime("%H:%M:%S")
		print(current_time)

		if now.second == start_time :

			print("새로고침")
			pyautogui.moveTo(click_xy[0],click_xy[1])
			pyautogui.click(button='left')
			chk_time=1
			print(current_time)

		time.sleep(0.5)
		now = datetime.now()


def keyboard_click():
	#시작 대기
	chk = 0
	while chk==0:
		if keyboard.is_pressed('enter'):
			print('  엔터 키 입력')
			time.sleep(0.1)
			chk=1
	chk=0


def click_table():

	#예측 클릭
	pyautogui.moveTo(click_5[0],click_5[1])
	pyautogui.click(button='left')
	pyautogui.moveTo(click_5[0]+10,click_5[1])
	pyautogui.click(button='left')


	#색상으로 구분해서 자동 클릭
	#클릭 2자리 완료되면 예매 완료 화면 이동
	chk_click=0
	chk_table=0
	while chk_table==0:
		pos = pyautogui.position()
		screen = ImageGrab.grab()
		color = screen.getpixel(pos)
		color = list(color)

		for c in chk_color :
			if c == color :
				pyautogui.click(button='left')

				print("click")
				print(color)
				chk_click=chk_click+1

		if chk_click==2:
			chk_table=1


if __name__ :
	
	#서버 시간 기다렸다 새로고침
	start()

	#방지 팝업 클릭
	print("1. 방지 클릭 : Enter")
	keyboard_click()
	pyautogui.moveTo(click_1[0],click_1[1])
	pyautogui.click(button='left')
	time.sleep(0.1)
	pyautogui.moveTo(1336,543)
	print("")
	

	#보안문자입력 이동
	print("2. 보안문자 입력 이동")
	keyboard_click()
	pyautogui.moveTo(click_2[0],click_2[1])
	pyautogui.click(button='left')
	print("")


	print("3. 보안문자 입력 완료")
	keyboard_click()
	pyautogui.moveTo(click_3[0],click_3[1])
	pyautogui.click(button='left')
	print("")
	

	#구역 선택 이동
	print("4.구역 이동 및 클릭")
	keyboard_click()
	pyautogui.moveTo(click_4[0],click_4[1])
	pyautogui.click(button='left')
	print("")

	
	#좌석 클릭
	print("5. 좌석이동")
	keyboard_click()
	click_table()
	

	#좌석선택완료 버튼 클릭
	print("6. 좌석선택완료 클릭")
	keyboard_click()
	pyautogui.moveTo(click_6[0],click_6[1])
	pyautogui.click(button='left')

	print("종료")
