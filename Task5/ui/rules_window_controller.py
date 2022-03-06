from PyQt5 import QtWidgets, uic


class RulesWindow(QtWidgets.QMainWindow):
    def __init__(self, menu_window):
        super(RulesWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/rules.ui', self)

        self.menuButton.clicked.connect(self.menu_btn_clicked)

    def menu_btn_clicked(self):
        self.menu_window.show()
        self.close()
