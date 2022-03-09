import random
from .game_field_item import GameFieldItem


class Game:
    _game_field_rows_count = 7
    _game_field_cols_count = 9
    _game_field = []

    def __init__(self):
        self._game_field = self._new_game_field()

    def _new_game_field(self):
        game_field = []
        for row in range(0, self._game_field_rows_count):
            new_row = []
            for col in range(0, self._game_field_cols_count):
                game_field_item: GameFieldItem = GameFieldItem(row, col, random.randint(1, 3))
                new_row.append(game_field_item)
            game_field.append(new_row)

        return game_field

    def get_game_field(self):
        return self._game_field
