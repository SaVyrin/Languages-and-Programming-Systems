from PyQt5 import QtWidgets
from Task5.ui.menu_window_controller import MenuWindow
import sys


def start():
    app = QtWidgets.QApplication([])
    main_window = MenuWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start()
