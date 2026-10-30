#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def process_zoo(zoo, birds):
    """Выполняет все операции над списком зоопарка."""
    zoo.insert(1, 'bear')          # медведь между львом и кенгуру
    zoo.extend(birds)              # птицы в конец
    zoo.remove('elephant')         # убрать слона
    lion_cell = zoo.index('lion') + 1
    lark_cell = zoo.index('lark') + 1
    return zoo, lion_cell, lark_cell


if __name__ == '__main__':
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    result, lion_cell, lark_cell = process_zoo(zoo, birds)
    print(result)
    print(f'Лев сидит в клетке {lion_cell}')
    print(f'Жаворонок сидит в клетке {lark_cell}')