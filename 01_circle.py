#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PI = 3.1415926


def circle_area(radius):
    """Площадь круга с точностью до 4 знаков."""
    return round(PI * radius ** 2, 4)


def is_point_in_circle(point, radius):
    """True, если точка внутри круга с центром (0,0)."""
    x, y = point
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance <= radius


if __name__ == '__main__':
    radius = 42
    print(circle_area(radius))
    print(is_point_in_circle((23, 34), radius))
    print(is_point_in_circle((30, 30), radius))