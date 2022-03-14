from .color import Color


class GameFieldItem:
    _x = 0
    _y = 0
    _color = Color.DEFAULT

    def __init__(self, x, y, value):
        self._x = x
        self._y = y
        self._color = self._convert_value_to_color(value)

    @staticmethod
    def _convert_value_to_color(value):
        for color in Color:
            if color.value == value:
                return color

    def get_color(self):
        return self._color

    def get_row(self):
        return self._x

    def get_col(self):
        return self._y
