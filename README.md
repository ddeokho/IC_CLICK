# CLICK

학습목적으로만 사용합니다.

#### 환경설정

1. 설치 모듈 설치
 - Listener
 - pillow
 - pyautogui
 - keyboard
 - ImageGrab
 - datetime
 
```
pip install 모듈명
```


2. .py 설명
- click.py: 좌표 얻기, 마우스로 클릭할 때마다 좌표를 가져옴
- click_bot.py: enter를 클릭할 때 마다 화면 내에 마우스가 이동하면서 각 미션을 수행
  (움직일 좌표를 업데이트해야 함.)


3. 파이썬 파일 실행 방법
```
(base)PS C:\user\경로>python click.py
(base)PS C:\user\경로>python click_bot.py
```


4. click_bot.py 실행 : 59초 도달 시 새로고침 진행 후 
 
 1) 첫 번째: enter
  -> 방지 팝업창 닫기 이동/클릭 + 버튼 쪽 이동
![image](https://user-images.githubusercontent.com/20199818/195015985-f9dbe744-a663-45f4-b0ef-3c122696bc79.png)
![image](https://user-images.githubusercontent.com/20199818/195025701-c39b9188-0851-4088-b1c5-b560c5cc8e81.png)



 
 2) 두 번째: enter -> [보안문자입력] 이동 + 클릭(바로 글 작성할 수 있도록 활성화)
 3) 세 번쨰: enter -> 작성 완료 후 enter를 치면 [입력완료]가 클릭됨. 마우스로 클릭하는 것보다 빠름
![image](https://user-images.githubusercontent.com/20199818/195026774-84014f07-2448-4ea9-b4ee-82d79e2d0422.png)
  
  

 4) 네 번째: enter
  -> 구역 선택 이동
![image](https://user-images.githubusercontent.com/20199818/195031267-b738d118-e25c-4394-a1ea-968babe864ce.png)


  
 5) 다섯 번째: enter(좌석 선택)
  -> 자동 좌석 클릭, 빈 곳의 색상을 확인해서 자동 클릭
  
  ![image](https://user-images.githubusercontent.com/20199818/195030945-27dc5b44-aa1a-4dca-be0a-c0665f03cb99.png)
  
  
  
 6) 여섯 번째: enter
  -> 좌석선택완료
  
 
 ![image](https://user-images.githubusercontent.com/20199818/195030343-91f3768e-f0f5-4fae-b57d-2952df23af32.png)
 
 
 5. 터미널 실행 강제종료 방법
```
Ctrl+c 
```


