from PyQt5 import QtWidgets, uic

from .about_window_controller import AboutWindow
from .game_window_controller import GameWindow
from .rules_window_controller import RulesWindow
from .settings_window_controller import SettingsWindow


class MenuWindow(QtWidgets.QMainWindow):
    _game_settings = {"color_mode": 0, "rows_count": 7, "cols_count": 9, "max_score": 0}

    def __init__(self):
        super(MenuWindow, self).__init__()
        self.next_window = None
        uic.loadUi('Resources/ui/forms/menu.ui', self)

        self.startButton.clicked.connect(self._start_btn_clicked)
        self.rulesButton.clicked.connect(self._rules_btn_clicked)
        self.settingsButton.clicked.connect(self._settings_btn_clicked)
        self.aboutButton.clicked.connect(self._about_btn_clicked)

    def get_game_settings(self):
        return self._game_settings

    def _start_btn_clicked(self):
        self.next_window = GameWindow(self, self._game_settings)
        self.next_window.show()
        self.hide()

    def _rules_btn_clicked(self):
        self.next_window = RulesWindow(self)
        self.next_window.show()
        self.hide()

    def _settings_btn_clicked(self):
        self.next_window = SettingsWindow(self, self._game_settings)
        self.next_window.show()
        self.hide()

    def _about_btn_clicked(self):
        self.next_window = AboutWindow(self)
        self.next_window.show()
        self.hide()
