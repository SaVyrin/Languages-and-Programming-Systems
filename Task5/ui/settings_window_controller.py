from PyQt5 import QtWidgets, uic


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, menu_window):
        super(SettingsWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/settings.ui', self)

        self.menuButton.clicked.connect(self.menu_btn_clicked)

    def menu_btn_clicked(self):
        self.menu_window.show()
        self.close()
