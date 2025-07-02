## Ex 3-1. 창 띄우기.
import sys
from PyQt5.QtWidgets import QApplication, QWidget

#Qwidget = 부모 클래스
# 부모 클래스를 상속받아서 MyApp이라는 클래스 생성
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # btn = QP
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 300)
        self.show()


if __name__ == '__main__':  
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
