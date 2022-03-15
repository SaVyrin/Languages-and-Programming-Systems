import random

from .color import Color


class GameFieldItem:
    _x = 0
    _y = 0
    _color = Color.DEFAULT

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.set_random_color()

    def set_color(self, color: Color):
        self._color = color

    def set_random_color(self):
        value = random.randint(1, 5)
        self._color = self._convert_value_to_color(value)

    @staticmethod
    def _convert_value_to_color(value):
        color_index = 0
        for color in Color:
            if color_index == value:
                return color
            color_index += 1

    def get_color(self):
        return self._color

    def get_row(self):
        return self._x

    def get_col(self):
        return self._y
