import sys
from PyQt6.QtWidgets import QApplication, QFrame, QVBoxLayout, QWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

# Box frame
box = QFrame()
box.setFrameShape(QFrame.Shape.Box)
box.setFrameShadow(QFrame.Shadow.Raised)
layout.addWidget(QLabel("Box Frame"))
layout.addWidget(box)

# Panel frame
panel = QFrame()
panel.setFrameShape(QFrame.Shape.Panel)
panel.setFrameShadow(QFrame.Shadow.Sunken)
layout.addWidget(QLabel("Panel Frame"))
layout.addWidget(panel)

# Horizontal line
hline = QFrame()
hline.setFrameShape(QFrame.Shape.HLine)
hline.setFrameShadow(QFrame.Shadow.Sunken)
layout.addWidget(QLabel("Horizontal Line"))
layout.addWidget(hline)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
