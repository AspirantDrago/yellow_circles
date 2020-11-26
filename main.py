import sys
import random

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic

from ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.painted = False
        self.setupUi(self)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        self.painted = True
        self.repaint()

    def paintEvent(self, event):
        if self.painted:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ))
        radius = random.randint(10, min(self.WIDTH, self.HEIGHT) // 2)
        x = random.randint(radius, self.WIDTH - radius)
        y = random.randint(radius, self.HEIGHT - radius)
        qp.drawEllipse(QPoint(x, y), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
