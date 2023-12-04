import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Draw_Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_draw = True
        self.btn_draw.clicked.connect(self.paint)

    def paint(self):
        self.do_draw = True
        self.update()

    def paintEvent(self, event):
        if self.do_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        color = QColor(255, 255, 0)
        x, y = randrange(10, 790), randrange(10, 590)
        d = randrange(2, min(x, y, 800 - x, 600 - y) // 2)
        qp.setBrush(color)
        qp.drawEllipse(x - d // 2, y - d // 2, d, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Draw_Circles()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
