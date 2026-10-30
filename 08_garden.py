#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garden_operations(garden, meadow):
    """Возвращает множества по заданию."""
    garden_set = set(garden)
    meadow_set = set(meadow)
    all_flowers = garden_set | meadow_set
    both = garden_set & meadow_set
    only_garden = garden_set - meadow_set
    only_meadow = meadow_set - garden_set
    return all_flowers, both, only_garden, only_meadow


if __name__ == '__main__':
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка',
              'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер',
              'мак', 'одуванчик', 'ромашка')
    all_f, both, only_g, only_m = garden_operations(garden, meadow)
    print('Все виды:', all_f)
    print('И там и там:', both)
    print('Только в саду:', only_g)
    print('Только на лугу:', only_m)