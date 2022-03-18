import time

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel

from .button import PushButton
from .finish_dialog_controller import FinishDialog
from ..game.game_controller import GameController
from ..game.game_field_item import GameFieldItem


class GameWindow(QtWidgets.QMainWindow):
    _game_controller: GameController = GameController()
    _grid_buttons: list

    def __init__(self, menu_window, game_settings):
        super(GameWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/game.ui', self)

        self._game_controller.set_game_settings(game_settings)
        self.menuButton.clicked.connect(self.menu_btn_clicked)
        self.current_score_label.setStyleSheet("QLabel{font-size: 14pt; qproperty-alignment: AlignCenter;}")
        self._grid_buttons = []
        self._init_game_elements()
        self._repaint_game_elements()

    def new_game(self):
        self._game_controller = GameController()
        self._repaint_game_elements()
        self._update_score_label()

    def update_time_label(self):
        label: QLabel = self.time_label
        while True:
            game_time = self._game_controller.get_game_time()
            label.setText(str(game_time))
            time.sleep(1000)

    def _check_if_game_finished(self):
        if self._game_controller.check_if_game_finished():
            my_dialog = FinishDialog(self)
            my_dialog.exec_()

    def _update_score_label(self):
        label: QLabel = self.current_score_label
        current_score = self._game_controller.get_game_score()
        label.setText(str(current_score))

    def clicked_event(self):
        button: PushButton = self.sender()
        self._game_controller.check_clicked_item(button)
        self._repaint_game_elements()
        self._update_score_label()
        self._check_if_game_finished()

    def menu_btn_clicked(self):
        self.menu_window.show()
        self.close()

    def _init_game_elements(self):
        game_field_elements: list = self._game_controller.get_game_field_elements()
        game_field_item: GameFieldItem
        for game_field_row in game_field_elements:
            buttons_row = []
            for game_field_item in game_field_row:
                row = game_field_item.get_row()
                col = game_field_item.get_col()

                button = PushButton(row, col, self)
                button.clicked.connect(self.clicked_event)
                buttons_row.append(button)
                self.gridLayout.addWidget(button, row + 1, col)
            self._grid_buttons.append(buttons_row)

    def _repaint_game_elements(self):
        game_field_elements: list = self._game_controller.get_game_field_elements()
        game_field_item: GameFieldItem
        for game_field_row in game_field_elements:
            for game_field_item in game_field_row:
                row = game_field_item.get_row()
                col = game_field_item.get_col()
                game_field_item_color_string = game_field_item.get_color().value

                button: PushButton = self._grid_buttons[row][col]
                button.setStyleSheet("background-color : " + game_field_item_color_string)
