from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout, QCheckBox, QComboBox, QSpinBox, QLabel, QPushButton, QLineEdit, \
    QWidget

from newPthon.newone.MyMain import MyMain,mymainrun


class DifferentQt(MyMain):
    def __init__(self):
        MyMain.__init__(self)
        self.setWindowTitle("Different Qt")

        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.update_style)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)

        cb = QCheckBox("Show Different Qt")
        layout.addWidget(cb)

        combo = QComboBox()
        combo.setObjectName("combo")
        combo.addItems(["first","second","third"])
        layout.addWidget(combo)

        sb = QSpinBox(self)
        sb.setRange(1, 999)
        layout.addWidget(sb)

        label = QLabel(self)
        label.setText("Label")
        layout.addWidget(label)

        le = QLineEdit(self)
        le.setObjectName("le")
        layout.addWidget(le)

        bp = QPushButton("Show Different Qt")
        layout.addWidget(bp)

        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

    def update_style(self):
        qss = self.editor.toPlainText()
        self.editor.setStyleSheet(qss)



mymainrun(DifferentQt)