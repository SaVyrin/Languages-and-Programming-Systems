from PyQt5 import QtWidgets, uic

finish_dialog_style_sheet = """
QDialog {
    border-image: url(Resources/images/finish_bckg.jpg) 0 0 0 0 stretch stretch;
}
QPushButton {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #111;
}

QPushButton:hover {
    background-color: rgba(232, 228, 216, 0.5);
    border: 3px solid #111;
}
QPushButton:pressed {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #aaa;
}
"""


class FinishDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(FinishDialog, self).__init__()
        uic.loadUi('Resources/ui/forms/finish_dialog.ui', self)

        self.setStyleSheet(finish_dialog_style_sheet)

        self._parent = parent
        self.menuButton.clicked.connect(self._menu_btn_clicked)
        self.newGameButton.clicked.connect(self._new_game_btn_clicked)

    def _menu_btn_clicked(self):
        self.hide()
        self._parent.menu_window.show()
        self.close()

    def _new_game_btn_clicked(self):
        parent = self._parent
        parent.new_game()
        self.close()
