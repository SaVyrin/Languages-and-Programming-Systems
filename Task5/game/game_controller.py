from Task5.game.game import Game
from Task5.ui.button import PushButton


class GameController:
    _last_clicked_item: PushButton = None
    _game: Game

    def __init__(self):
        self._game = Game()

    def get_game_field_elements(self):
        return self._game.get_game_field_elements()

    def check_clicked_item(self, clicked_item: PushButton):
        if self._last_clicked_item is None:
            self._last_clicked_item = clicked_item
            return

        if self._last_clicked_item == clicked_item:
            return

        if self._check_neighbours(self._last_clicked_item, clicked_item):
            first_row = self._last_clicked_item.get_row()
            first_col = self._last_clicked_item.get_col()
            second_row = clicked_item.get_row()
            second_col = clicked_item.get_col()

            self._game.make_move(first_row, first_col, second_row, second_col)
            self._last_clicked_item = None
        else:
            self._last_clicked_item = clicked_item

    @staticmethod
    def _check_neighbours(first_item: PushButton, second_item: PushButton):
        first_row = first_item.get_row()
        first_col = first_item.get_col()

        second_row = second_item.get_row()
        second_col = second_item.get_col()

        up_neighbour: bool = (first_row - 1) == second_row and first_col == second_col
        down_neighbour: bool = (first_row + 1) == second_row and first_col == second_col
        left_neighbour: bool = first_row == second_row and (first_col - 1) == second_col
        right_neighbour: bool = first_row == second_row and (first_col + 1) == second_col

        if up_neighbour or down_neighbour or left_neighbour or right_neighbour:
            return True

        return False
