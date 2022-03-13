from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor
from ..game.color import Color
from ..game.game import Game


class GameWindow(QtWidgets.QMainWindow):
    _game: Game = Game()

    def __init__(self, menu_window):
        super(GameWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/game.ui', self)

        self.menuButton.clicked.connect(self.menu_btn_clicked)
        table: QtWidgets.QTableWidget = self.tableWidget

        table.setRowCount(7)
        table.setColumnCount(9)

        table.setFixedWidth(542)
        table.setFixedHeight(422)
        width = table.width()
        height = table.height()
        table.horizontalHeader().setDefaultSectionSize(int(width / 9))
        table.verticalHeader().setDefaultSectionSize(int(height / 7))
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        self.init_table(table)
        self.repaint_table(table)

    def menu_btn_clicked(self):
        self.menu_window.show()
        self.close()

    @staticmethod
    def init_table(table):
        for row in range(0, 7):
            for col in range(0, 9):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(col))

    def repaint_table(self, table):
        for row in range(0, 7):
            for col in range(0, 9):
                item: QtWidgets.QTableWidgetItem = table.item(row, col)

                color = self.choose_color(self._game.get_item_color(row, col))
                item.setBackground(color)

    @staticmethod
    def choose_color(color: Color):
        if color == Color.DEFAULT:
            return QColor("#fff")
        if color == Color.RED:
            return QColor("#FF0000")
        if color == Color.ORANGE:
            return QColor("#FFA500")
        if color == Color.YELLOW:
            return QColor("#FFFF00")
        if color == Color.BLUE:
            return QColor("#42AAFF")
        if color == Color.VIOLET:
            return QColor("#9966CC")
