from kiwoom.kiwoom import *

import sys #어디에 
from PyQt5.QtWidgets import *

class Ui_class():
    def __init__(self):
        print("Ui_class 입니다")

        self.app=QApplication(sys.argv) #UI를 실행하기위해 초기화 시켜주는 함수
        #argv: 파이썬 경로가 담겨져 있다.


        self.kiwoom = Kiwoom()

        self.app.exec_() #이벤트 루프를 실행시켜 주는 것

