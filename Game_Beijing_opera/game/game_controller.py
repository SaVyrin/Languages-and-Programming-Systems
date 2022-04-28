from Game_Beijing_opera.game.game import Game
from Game_Beijing_opera.ui.button import PushButton


class GameController:
    _last_clicked_item: PushButton = None
    _game: Game
    _color_mode = 0
    _rows_count = 5
    _cols_count = 7
    _max_score = 0

    def __init__(self, game_settings: dict):
        self.set_game_settings(game_settings)
        self._new_game()

    def set_game_settings(self, game_settings: dict):
        color_mode = game_settings["color_mode"]
        rows_count = game_settings["rows_count"]
        cols_count = game_settings["cols_count"]
        max_score = game_settings["max_score"]

        self._change_color_mode(color_mode)
        self._change_game_field_size(rows_count, cols_count)
        self._change_max_score(max_score)

    def get_game_score(self):
        return self._game.get_game_score()

    def get_game_max_score(self):
        return self._game.get_game_max_score()

    def get_moves_count(self):
        return self._game.get_game_moves_count()

    def check_if_game_finished(self):
        return self._game.is_game_finished()

    def _new_game(self):
        self._game = Game(self._color_mode, self._rows_count, self._cols_count, self._max_score)

    def _change_color_mode(self, color_mode):
        self._color_mode = color_mode

    def _change_game_field_size(self, rows_count, cols_count):
        self._rows_count = rows_count
        self._cols_count = cols_count

    def _change_max_score(self, max_score):
        self._max_score = max_score

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
