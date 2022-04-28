from PyQt5 import QtWidgets, uic


class AboutWindow(QtWidgets.QMainWindow):
    def __init__(self, menu_window):
        super(AboutWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/about.ui', self)

        self.menuButton.clicked.connect(self._menu_btn_clicked)

    def _menu_btn_clicked(self):
        self.menu_window.show()
        self.close()
