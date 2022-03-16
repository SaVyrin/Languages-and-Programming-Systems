from .game_field_item import GameFieldItem


class GameField:
    _GAME_FIELD_ROWS_COUNT = 7
    _GAME_FIELD_COLS_COUNT = 9

    _game_field = []

    def __init__(self):
        self._game_field = self._new_game_field()

    def get_game_elements(self):
        return self._game_field

    def _new_game_field(self):
        game_field = []
        for row in range(0, self._GAME_FIELD_ROWS_COUNT):
            new_row = []
            for col in range(0, self._GAME_FIELD_COLS_COUNT):
                game_field_item: GameFieldItem = GameFieldItem(row, col)
                new_row.append(game_field_item)
            game_field.append(new_row)

        return game_field

    def make_move(self, first_row, first_col, second_row, second_col):
        first_item: GameFieldItem = self._game_field[first_row][first_col]
        second_item: GameFieldItem = self._game_field[second_row][second_col]
        self._swap_colors(first_item, second_item)
        bitten_items = self._get_bitten_items(first_item, second_item)

        self._new_random_bitten_colors(bitten_items)
        self._move_bitten_colors_to_top(bitten_items)

        bitten_items_count = len(bitten_items)
        if bitten_items_count == 0:
            self._swap_colors(first_item, second_item)
        return bitten_items_count

    @staticmethod
    def _swap_colors(first_item: GameFieldItem, second_item: GameFieldItem):
        first_item_color = first_item.get_color()
        second_item_color = second_item.get_color()
        first_item.set_color(second_item_color)
        second_item.set_color(first_item_color)

    def _move_bitten_colors_to_top(self, bitten_items):
        item: GameFieldItem
        bitten_items.sort(key=lambda item: item.get_row(), )
        for item in bitten_items:
            item_row = item.get_row()
            item_col = item.get_col()

            while item_row > 0:
                prev_item = self._game_field[item_row][item_col]
                next_item = self._game_field[item_row - 1][item_col]
                next_item_color = next_item.get_color()
                prev_item_color = prev_item.get_color()

                prev_item.set_color(next_item_color)
                next_item.set_color(prev_item_color)

                item_row -= 1

    @staticmethod
    def _new_random_bitten_colors(bitten_items):
        item: GameFieldItem
        for item in bitten_items:
            item.set_random_color()

    def _get_bitten_items(self, first_item: GameFieldItem, second_item: GameFieldItem):
        bitten_total = set()

        first_item_bitten_vertical = self._get_bitten_vertical(first_item)
        first_item_bitten_horizontal = self._get_bitten_horizontal(first_item)

        second_item_bitten_vertical = self._get_bitten_vertical(second_item)
        second_item_bitten_horizontal = self._get_bitten_horizontal(second_item)

        if len(first_item_bitten_vertical) >= 3:
            bitten_total.update(first_item_bitten_vertical)

        if len(first_item_bitten_horizontal) >= 3:
            bitten_total.update(first_item_bitten_horizontal)

        if len(second_item_bitten_vertical) >= 3:
            bitten_total.update(second_item_bitten_vertical)

        if len(second_item_bitten_horizontal) >= 3:
            bitten_total.update(second_item_bitten_horizontal)

        return list(bitten_total)

    def _get_bitten_vertical(self, item: GameFieldItem):
        bitten_list = [item]

        item_row = item.get_row()
        item_col = item.get_col()
        item_color = item.get_color()

        up_row = item_row - 1
        while up_row >= 0:
            current_item = self._game_field[up_row][item_col]
            if item_color == current_item.get_color():
                bitten_list.append(current_item)
            else:
                break

            up_row -= 1

        down_row = item_row + 1
        while down_row <= (self._GAME_FIELD_ROWS_COUNT - 1):
            current_item = self._game_field[down_row][item_col]
            if item_color == current_item.get_color():
                bitten_list.append(current_item)
            else:
                break

            down_row += 1

        return bitten_list

    def _get_bitten_horizontal(self, item: GameFieldItem):
        bitten_list = [item]

        item_row = item.get_row()
        item_col = item.get_col()
        item_color = item.get_color()

        left_col = item_col - 1
        while left_col >= 0:
            current_item = self._game_field[item_row][left_col]
            if item_color == current_item.get_color():
                bitten_list.append(current_item)
            else:
                break

            left_col -= 1

        right_col = item_col + 1
        while right_col <= (self._GAME_FIELD_COLS_COUNT - 1):
            current_item = self._game_field[item_row][right_col]
            if item_color == current_item.get_color():
                bitten_list.append(current_item)
            else:
                break

            right_col += 1

        return bitten_list
