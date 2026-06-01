import sys
import time
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class MainStopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.elapsed_time = 0
        self.start_time = 0

        self.setWindowTitle("Stopwatch")
        self.setGeometry(300, 300, 400, 200)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.time_label = QLabel("00:00:00")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 48px;
            font-weight: bold;
        """)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        self.start_button.clicked.connect(self.handle_start)
        self.stop_button.clicked.connect(self.handle_end)
        self.reset_button.clicked.connect(self.handle_reset_time)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.time_label)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def format_time(self, milliseconds):
        total_seconds = milliseconds // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def handle_start(self):
        if not self.timer.isActive():
            self.start_time = int(time.time() * 1000) - self.elapsed_time
            self.timer.start(1000)

    def update_time(self):
        self.elapsed_time = int(time.time() * 1000) - self.start_time
        self.time_label.setText(self.format_time(self.elapsed_time))

    def handle_end(self):
        self.timer.stop()

    def handle_reset_time(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.time_label.setText("00:00:00")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainStopWatch()
    window.show()

    sys.exit(app.exec())