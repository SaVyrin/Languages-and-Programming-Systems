from PyQt5 import QtWidgets, uic, QtGui

about_style_sheet = """
AboutWindow {
    border-image: url(Resources/images/bckg.jpg) 0 0 0 0 stretch stretch;
}
QPushButton {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #111;
}

QPushButton:hover {
    background-color: rgba(183, 30, 28, 0.8);
    border: 3px solid #111;
}
QPushButton:pressed {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #aaa;
}
"""


class AboutWindow(QtWidgets.QMainWindow):
    def __init__(self, menu_window):
        super(AboutWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/about.ui', self)

        self.setStyleSheet(about_style_sheet)
        self.setWindowIcon(QtGui.QIcon('Resources/images/icon.png'))

        self.menuButton.clicked.connect(self._menu_btn_clicked)

    def _menu_btn_clicked(self):
        self.menu_window.show()
        self.close()
