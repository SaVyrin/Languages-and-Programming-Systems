from PyQt5 import QtWidgets, uic

from .button import PushButton
from ..game.game_controller import GameController
from ..game.game_field_item import GameFieldItem


class GameWindow(QtWidgets.QMainWindow):
    _game_controller: GameController
    _grid_buttons: list

    def __init__(self, menu_window):

        super(GameWindow, self).__init__()
        self.menu_window = menu_window
        uic.loadUi('Resources/ui/forms/game.ui', self)

        self._game_controller = GameController()

        self.menuButton.clicked.connect(self.menu_btn_clicked)
        self._grid_buttons = []
        self._init_game_elements()
        self._repaint_game_elements()

    def clicked_event(self):
        button: PushButton = self.sender()
        self._game_controller.check_clicked_item(button)
        self._repaint_game_elements()

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

#      TODO : add  make_move and get_game_field -> repaint
