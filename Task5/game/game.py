from .game_field import GameField
from .game_state import GameState


class Game:
    _ONE_BITTEN_ITEM_POINTS = 100

    _game_state = GameState.NOT_STARTED
    _game_score = 0
    _game_max_score = 0
    _game_moves_count = 0

    def __init__(self, color_mode, rows_count, cols_count, max_score):
        self._game_field = GameField(color_mode, rows_count, cols_count)
        self._game_state = GameState.NOT_STARTED
        self._game_score = 0
        self._game_max_score = max_score
        self._game_moves_count = 20

    def make_move(self, first_row, first_col, second_row, second_col):
        items_bitten_count = self._game_field.make_move(first_row, first_col, second_row, second_col)
        self._add_score(items_bitten_count)
        self.decrease_moves_count()
        self._check_finish_game()

    def is_game_finished(self):
        if self._game_state == GameState.FINISHED:
            return True
        return False

    def get_game_score(self):
        return self._game_score

    def get_game_max_score(self):
        return self._game_max_score

    def get_game_moves_count(self):
        return self._game_moves_count

    def get_game_field_elements(self):
        return self._game_field.get_game_elements()

    def _add_score(self, items_bitten_count):
        score_to_add = self._ONE_BITTEN_ITEM_POINTS * items_bitten_count
        self._game_score += score_to_add

        if self._game_max_score < self._game_score:
            self._game_max_score = self._game_score

    def _check_finish_game(self):
        if self._game_moves_count <= 0:
            self._finish_game()

    def _finish_game(self):
        self._game_state = GameState.FINISHED

    def decrease_moves_count(self):
        self._game_moves_count -= 1
