from PyQt5 import QtWidgets, uic
from .game_window_controller import GameWindow
from .rules_window_controller import RulesWindow
from .settings_window_controller import SettingsWindow


class MenuWindow(QtWidgets.QMainWindow):
    _game_settings = {"color_mode": 0, "rows_count": 7, "cols_count": 9}

    def __init__(self):
        super(MenuWindow, self).__init__()
        self.next_window = None
        uic.loadUi('Resources/ui/forms/menu.ui', self)

        self.startButton.clicked.connect(self.start_btn_clicked)
        self.rulesButton.clicked.connect(self.rules_btn_clicked)
        self.settingsButton.clicked.connect(self.settings_btn_clicked)

    def get_game_settings(self):
        return self._game_settings

    def start_btn_clicked(self):
        self.next_window = GameWindow(self, self._game_settings)
        self.next_window.show()
        self.hide()

    def rules_btn_clicked(self):
        self.next_window = RulesWindow(self)
        self.next_window.show()
        self.hide()

    def settings_btn_clicked(self):
        self.next_window = SettingsWindow(self, self._game_settings)
        self.next_window.show()
        self.hide()
