import sys
import random

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.WIDTH = 300
        self.HEIGHT = 300
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, self.WIDTH, self.HEIGHT)
        self.btn = QPushButton('Создать окружность', self)
        self.btn.resize(self.WIDTH - 40, 40)
        self.btn.move(20, self.HEIGHT - 40 - 10)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = random.randint(10, min(self.WIDTH, self.HEIGHT) // 2)
        x = random.randint(radius, self.WIDTH - radius)
        y = random.randint(radius, self.HEIGHT - radius)
        qp.drawEllipse(QPoint(x, y), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
