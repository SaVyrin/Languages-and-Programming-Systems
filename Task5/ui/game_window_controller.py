from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QLabel

from .button import PushButton
from .finish_dialog_controller import FinishDialog
from ..game.game_controller import GameController
from ..game.game_field_item import GameFieldItem

game_style_sheet = """
GameWindow {
    border-image: url(Resources/images/game_bckg.jpg) 0 0 0 0 stretch stretch;
}
QPushButton#menuButton {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #111;
}

QPushButton#menuButton:hover {
    background-color: rgba(183, 30, 28, 0.8);
    border: 3px solid #111;
}
QPushButton#menuButton:pressed {
    background-color: rgba(232, 228, 216, 0.8);
    border: 3px solid #aaa;
}
"""


class GameWindow(QtWidgets.QMainWindow):
    _game_controller: GameController
    _grid_buttons: list

    def __init__(self, menu_window, game_settings):
        super(GameWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/game.ui', self)

        self.setWindowIcon(QtGui.QIcon('Resources/images/icon.png'))
        self.setStyleSheet(game_style_sheet)

        self._game_settings = game_settings
        self._game_controller: GameController = GameController(game_settings)

        self.menuButton.clicked.connect(self.menu_btn_clicked)
        self._grid_buttons = []
        self._init_game_elements()
        self._update_ui()

    def new_game(self):
        self._game_controller = GameController(self._game_settings)
        self._update_ui()

    def _check_if_game_finished(self):
        if self._game_controller.check_if_game_finished():
            game_settings = self.menu_window.get_game_settings()
            game_settings["max_score"] = self._game_controller.get_game_max_score()
            self._game_settings["max_score"] = self._game_controller.get_game_max_score()
            my_dialog = FinishDialog(self)
            my_dialog.exec_()

    def _update_ui(self):
        self._repaint_game_elements()
        self._update_score_label()
        self._update_moves_label()
        self._update_max_score_label()

    def _update_score_label(self):
        label: QLabel = self.current_score_label
        current_score = self._game_controller.get_game_score()
        label.setText(str(current_score))

    def _update_max_score_label(self):
        label: QLabel = self.maxScoreLabel
        current_moves_count = self._game_controller.get_game_max_score()
        label.setText(str(current_moves_count))

    def _update_moves_label(self):
        label: QLabel = self.movesLabel
        current_moves_count = self._game_controller.get_moves_count()
        label.setText(str(current_moves_count))

    def clicked_event(self):
        button: PushButton = self.sender()
        self._game_controller.check_clicked_item(button)
        self._update_ui()
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
