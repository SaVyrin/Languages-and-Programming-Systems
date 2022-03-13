import random
from .game_field_item import GameFieldItem
from .game_state import GameState


class Game:
    _game_field_rows_count = 7
    _game_field_cols_count = 9
    _game_field = []
    _game_state = GameState.NOT_STARTED

    def __init__(self):
        self._game_field = self._new_game_field()
        self._game_state = GameState.NOT_STARTED

    def _new_game_field(self):
        game_field = []
        for row in range(0, self._game_field_rows_count):
            new_row = []
            for col in range(0, self._game_field_cols_count):
                game_field_item: GameFieldItem = GameFieldItem(row, col, random.randint(1, 5))
                new_row.append(game_field_item)
            game_field.append(new_row)

        return game_field

    def get_game_field(self):
        return self._game_field

    def get_item_color(self, row, col):
        item: GameFieldItem = self._game_field[row][col]
        color = item.get_color()
        return color

    def start_game(self):
        self._game_state = GameState.PLAYING

    def stop_game(self):
        self._game_state = GameState.STOPPED

    def lose_game(self):
        self._game_state = GameState.LOST

    def win_game(self):
        self._game_state = GameState.WON

    def finish_game(self):
        self._game_state = GameState.NOT_STARTED
