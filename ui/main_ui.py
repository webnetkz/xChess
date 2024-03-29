from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont, QIcon

from components.button import createButton
from components.input import createInput


class MainWindowUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.old_pos = None

        layout = QVBoxLayout()
                
        layout.addWidget(createInput(self, 'Enter url game'))
        layout.addWidget(createButton(self, 'Close'))

        layout.addStretch()

        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        radius = 12
        background_color = QColor(0, 0, 0, 200)
        painter.setBrush(QBrush(background_color))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, radius, radius)

if __name__ == '__main__':
    app = QApplication([])

    app.setWindowIcon(QIcon("./logo.png"))

    w = MainWindowUI()
    w.resize(400, 100)
    w.show()

    app.exec()
