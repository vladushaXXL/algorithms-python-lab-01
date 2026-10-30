#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def father_height(family_height):
    """Рост отца."""
    for name, height in family_height:
        if name == 'папа':
            return height
    return None


def total_family_height(family_height):
    """Суммарный рост всех членов семьи."""
    return sum(height for _, height in family_height)


if __name__ == '__main__':
    my_family = ['мама', 'папа', 'брат', 'сестра', 'бабушка', 'дедушка']
    my_family_height = [
        ['мама', 165],
        ['папа', 180],
        ['брат', 175],
        ['сестра', 160],
        ['бабушка', 155],
        ['дедушка', 170],
    ]
    print(f'Рост отца - {father_height(my_family_height)} см')
    print(f'Общий рост моей семьи - {total_family_height(my_family_height)} см')