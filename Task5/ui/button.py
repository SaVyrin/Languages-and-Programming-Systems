from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    _row = 0
    _col = 0

    def __init__(self, row, col, parent=None):
        super(PushButton, self).__init__(parent)

        self._row = row
        self._col = col
        self.setMinimumSize(QSize(53, 50))
        self.setMaximumSize(QSize(58, 58))

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col
