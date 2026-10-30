#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculate_store(goods, store):
    """Возвращает список строк: <товар> - <кол-во> шт, стоимость <сумма> руб."""
    result = []
    for product_name, code in goods.items():
        total_quantity = 0
        total_cost = 0
        for batch in store[code]:
            total_quantity += batch['quantity']
            total_cost += batch['quantity'] * batch['price']
        result.append(
            f'{product_name} - {total_quantity} шт, стоимость {total_cost} руб'
        )
    return result


if __name__ == '__main__':
    goods = {'Лампа': '12345', 'Стол': '23456',
             'Диван': '34567', 'Стул': '45678'}
    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [{'quantity': 22, 'price': 510},
                  {'quantity': 32, 'price': 520}],
        '34567': [{'quantity': 2, 'price': 1200},
                  {'quantity': 1, 'price': 1150}],
        '45678': [{'quantity': 50, 'price': 100},
                  {'quantity': 12, 'price': 95},
                  {'quantity': 43, 'price': 97}],
    }
    for line in calculate_store(goods, store):
        print(line)