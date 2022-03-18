import time

from .game_field import GameField
from .game_state import GameState


class Game:
    _ONE_BITTEN_ITEM_POINTS = 100

    _game_state = GameState.NOT_STARTED
    _game_time = 0
    _game_score = 0
    _game_target_score = 0

    def __init__(self, color_mode, rows_count, cols_count):
        self._game_field = GameField(color_mode, rows_count, cols_count)
        self._game_state = GameState.NOT_STARTED
        self._game_time = 300
        self._game_score = 0
        self._game_target_score = 3000

    def make_move(self, first_row, first_col, second_row, second_col):
        items_bitten_count = self._game_field.make_move(first_row, first_col, second_row, second_col)
        self._add_score(items_bitten_count)
        self._check_win_score()

    def is_game_finished(self):
        if self._game_state == GameState.WON:
            return True
        return False

    def get_game_time(self):
        return self._game_time

    def get_game_score(self):
        return self._game_score

    def get_game_field_elements(self):
        return self._game_field.get_game_elements()

    def start_game(self):
        self._game_state = GameState.PLAYING
        self._decrease_time()

    def stop_game(self):
        self._game_state = GameState.STOPPED

    def finish_game(self):
        self._game_state = GameState.NOT_STARTED

    def _lose_game(self):
        self._game_state = GameState.LOST

    def _win_game(self):
        self._game_state = GameState.WON

    def _decrease_time(self):
        while self._game_state == GameState.PLAYING:
            self._game_time -= 1
            if self._game_time <= 0:
                self._game_state = GameState.LOST
            time.sleep(1000)

    def _add_score(self, items_bitten_count):
        score_to_add = self._ONE_BITTEN_ITEM_POINTS * items_bitten_count
        self._game_score += score_to_add

    def _check_win_score(self):
        if self._game_score >= self._game_target_score:
            self._game_score = self._game_target_score
            self._win_game()
