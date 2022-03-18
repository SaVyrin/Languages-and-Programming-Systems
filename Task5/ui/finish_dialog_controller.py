from PyQt5 import QtWidgets, uic


class FinishDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(FinishDialog, self).__init__()
        uic.loadUi('Resources/ui/forms/finish_dialog.ui', self)

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
