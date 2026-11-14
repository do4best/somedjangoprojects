import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QLabel, QHBoxLayout, QVBoxLayout

app = QApplication(sys.argv)

# --- Main Window ---
main_window = QWidget()
main_window.setWindowTitle("QWidget vs QFrame Comparison")

# Layout to hold both sections side by side
main_layout = QHBoxLayout()

# --- QWidget Section ---
widget_section = QWidget()
widget_layout = QVBoxLayout()
widget_layout.addWidget(QLabel("This is inside a QWidget"))
widget_section.setLayout(widget_layout)

# --- QFrame Section ---
frame_section = QFrame()
frame_section.setFrameShape(QFrame.Shape.Box)
frame_section.setFrameShadow(QFrame.Shadow.Raised)

frame_layout = QVBoxLayout()
frame_layout.addWidget(QLabel("This is inside a QFrame"))
frame_section.setLayout(frame_layout)

# Add both sections to the main layout
main_layout.addWidget(widget_section)
main_layout.addWidget(frame_section)

main_window.setLayout(main_layout)
main_window.resize(400, 150)
main_window.show()

sys.exit(app.exec())

