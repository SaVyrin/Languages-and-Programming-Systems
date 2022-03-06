import math


class Circle:
    _x = 0.0
    _y = 0.0
    _r = 0.0
    _area = 0.0
    _circles_in = 0

    def __init__(self, x, y, r):
        self._x = x
        self._y = y
        self._r = r
        self._area = math.pi * (r ** 2)

    def get_area(self):
        return self._area

    def set_circles_in(self, circles_in):
        self._circles_in = circles_in

    def get_circles_in(self):
        return self._circles_in

    def circle_in(self, other_circle):
        distance_between_centers = ((self._x - other_circle._x) ** 2 +
                                    (self._y - other_circle._y) ** 2) ** 0.5
        if (distance_between_centers + other_circle._r) <= self._r:
            return True
        else:
            return False

    def print(self):
        print("Circle: x = {} y = {} r = {} area = {} circles in = {}"
              .format(self._x, self._y, self._r, self._area, self._circles_in))
