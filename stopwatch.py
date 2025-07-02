import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import QTimer, Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch with Lap Time')
        self.setGeometry(300, 300, 400, 300)

        self.time = 0  # 0.1초 단위 시간
        self.lap_count = 1
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)

        # 시간 표시
        self.label = QLabel(self.format_time(self.time), self)
        self.label.setStyleSheet("font-size: 30px;")
        self.label.setAlignment(Qt.AlignCenter)

        # Lap 기록 창
        self.lap_log = QTextEdit(self)
        self.lap_log.setReadOnly(True)
        self.lap_log.setPlaceholderText("기록된 시간")

        # 버튼들
        self.btn_start = QPushButton('시작', self)
        self.btn_start.clicked.connect(self.start)

        self.btn_pause = QPushButton('일시정지', self)
        self.btn_pause.clicked.connect(self.pause)

        self.btn_reset = QPushButton('리셋', self)
        self.btn_reset.clicked.connect(self.reset)

        self.btn_lap = QPushButton('기록', self)
        self.btn_lap.clicked.connect(self.lap)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_start)
        button_layout.addWidget(self.btn_pause)
        button_layout.addWidget(self.btn_reset)
        button_layout.addWidget(self.btn_lap)

        # 전체 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(button_layout)
        vbox.addWidget(self.lap_log)

        self.setLayout(vbox)
        self.show()

    def format_time(self, t):
        minutes = t // 600
        seconds = (t % 600) // 10
        milliseconds = t % 10
        return f'{minutes:02}:{seconds:02}.{milliseconds}'

    def update_time(self):
        self.time += 1
        self.label.setText(self.format_time(self.time))

    def start(self):
        self.timer.start()

    def pause(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = 0
        self.label.setText(self.format_time(self.time))
        self.lap_count = 1
        self.lap_log.clear()

    def lap(self):
        if self.timer.isActive():
            lap_time = self.format_time(self.time)
            self.lap_log.append(f"[Lap {self.lap_count}] {lap_time}")
            self.lap_count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
