#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import pytest

m00 = importlib.import_module("00_distance")
m01 = importlib.import_module("01_circle")
m02 = importlib.import_module("02_operations")
m03 = importlib.import_module("03_favorite_movies")
m04 = importlib.import_module("04_my_family")
m05 = importlib.import_module("05_zoo")
m06 = importlib.import_module("06_songs_list")
m07 = importlib.import_module("07_secret")
m08 = importlib.import_module("08_garden")
m09 = importlib.import_module("09_shopping")
m10 = importlib.import_module("10_store")


# ---------- 00_distance ----------
def test_00_distances_symmetric():
    r = m00.get_distances({'A': (0, 0), 'B': (3, 4)})
    assert r['A']['B'] == 5.0
    assert r['B']['A'] == 5.0


def test_00_no_self_distance():
    r = m00.get_distances({'A': (0, 0), 'B': (1, 1)})
    assert 'A' not in r['A']
    assert 'B' not in r['B']


def test_00_three_cities():
    sites = {'A': (0, 0), 'B': (3, 4), 'C': (6, 8)}
    r = m00.get_distances(sites)
    assert r['A']['B'] == 5.0
    assert r['A']['C'] == 10.0
    assert r['B']['C'] == 5.0


# ---------- 01_circle ----------
def test_01_area():
    assert m01.circle_area(1) == 3.1416
    assert m01.circle_area(10) == 314.1593


@pytest.mark.parametrize('point, expected', [
    ((0, 0), True),
    ((0, 42), True),
    ((23, 34), True),
    ((30, 30), False),
    ((43, 0), False),
])
def test_01_point_in_circle(point, expected):
    assert m01.is_point_in_circle(point, 42) is expected


# ---------- 02_operations ----------
def test_02_make_25():
    assert m02.make_25() == 25


# ---------- 03_favorite_movies (возвращает кортеж!) ----------
def test_03_movies_parts():
    s = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    first, last, second, second_from_end = m03.get_movie_parts(s)
    assert first == 'Терминатор'
    assert last == 'Назад в будущее'
    assert second == 'Пятый элемент'
    assert second_from_end == 'Чужие'


# ---------- 04_my_family ----------
def test_04_father_height():
    heights = [['мама', 165], ['папа', 180], ['брат', 175]]
    assert m04.father_height(heights) == 180


def test_04_total_height():
    heights = [['мама', 165], ['папа', 180], ['брат', 175]]
    assert m04.total_family_height(heights) == 520


def test_04_missing_father_returns_none():
    # в 04 нет raise, при отсутствии отца возвращается None
    assert m04.father_height([['мама', 165]]) is None


# ---------- 05_zoo (мутирует входной список, возвращает кортеж) ----------
def test_05_process_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    updated, lion_cell, lark_cell = m05.process_zoo(zoo, birds)
    assert updated == ['lion', 'bear', 'kangaroo', 'monkey',
                       'rooster', 'ostrich', 'lark']
    assert lion_cell == 1
    assert lark_cell == 7


def test_05_process_zoo_mutates_input():
    # функция меняет список in-place и возвращает тот же объект
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    original_id = id(zoo)
    result, _, _ = m05.process_zoo(zoo, ['lark'])
    assert id(result) == original_id
    assert 'bear' in zoo
    assert 'elephant' not in zoo


# ---------- 06_songs_list ----------
def test_06_sum_list():
    songs = [['A', 1.1], ['B', 2.2], ['C', 3.3]]
    assert m06.sum_songs_list(songs, ['A', 'C']) == 4.4


def test_06_sum_list_empty():
    assert m06.sum_songs_list([['A', 1.0]], ['Z']) == 0.0


def test_06_sum_dict():
    d = {'A': 1.1, 'B': 2.2, 'C': 3.3}
    assert m06.sum_songs_dict(d, ['A', 'B']) == 3.3


def test_06_sum_dict_rounding():
    d = {'A': 1.111, 'B': 2.222, 'C': 3.333}
    assert m06.sum_songs_dict(d, ['A', 'B', 'C']) == 6.666


# ---------- 07_secret ----------
# В самом файле строки в cp1251-кракозябрах, поэтому проверяем
# ИМЕННО ЛОГИКУ срезов на синтетических данных с известными индексами.
def test_07_secret_logic():
    secret = [
        'abcdef',                    # [3]      = 'd'
        '0123456789abcdef',          # [9:13]   = '9abc'
        '0123456789abcdefghij',      # [5:15:2] = '579bd'
        '0123456789abcdefghij',      # [12:6:-1] = 'cba987'
        '0123456789abcdefghijk',     # [20:15:-1] = 'kjihg'
    ]
    assert m07.decrypt_message(secret) == 'd 9abc 579bd cba987 kjihg'


def test_07_secret_format():
    secret = [
        'abcde',
        'abcdefghijklm',
        'abcdefghijklmnop',
        'abcdefghijklmnop',
        'abcdefghijklmnopqrstu',
    ]
    result = m07.decrypt_message(secret)
    assert len(result.split(' ')) == 5


# ---------- 08_garden (возвращает кортеж из 4 множеств) ----------
def test_08_sets():
    g = ('роза', 'ромашка')
    m = ('ромашка', 'клевер')
    all_f, both, only_g, only_m = m08.garden_operations(g, m)
    assert all_f == {'роза', 'ромашка', 'клевер'}
    assert both == {'ромашка'}
    assert only_g == {'роза'}
    assert only_m == {'клевер'}


def test_08_duplicates_removed():
    g = ('роза', 'роза', 'ромашка')
    m = ('ромашка', 'ромашка')
    all_f, both, only_g, only_m = m08.garden_operations(g, m)
    assert all_f == {'роза', 'ромашка'}
    assert both == {'ромашка'}
    assert only_g == {'роза'}
    assert only_m == set()


# ---------- 09_shopping ----------
def test_09_cheapest_two():
    shops = {
        's1': [{'name': 'яблоко', 'price': 100}],
        's2': [{'name': 'яблоко', 'price': 80}],
        's3': [{'name': 'яблоко', 'price': 90}],
    }
    r = m09.find_best_prices(shops)
    assert len(r['яблоко']) == 2
    assert r['яблоко'][0]['shop'] == 's2'
    assert r['яблоко'][0]['price'] == 80
    assert r['яблоко'][1]['shop'] == 's3'
    assert r['яблоко'][1]['price'] == 90


def test_09_multiple_products():
    shops = {
        's1': [{'name': 'a', 'price': 5}, {'name': 'b', 'price': 10}],
        's2': [{'name': 'a', 'price': 3}, {'name': 'b', 'price': 20}],
    }
    r = m09.find_best_prices(shops)
    assert r['a'][0]['shop'] == 's2'
    assert r['a'][0]['price'] == 3
    assert r['b'][0]['shop'] == 's1'
    assert r['b'][0]['price'] == 10


# ---------- 10_store (возвращает список строк) ----------
def test_10_store():
    goods = {'Лампа': '1'}
    store = {'1': [{'quantity': 2, 'price': 100},
                   {'quantity': 3, 'price': 200}]}
    assert m10.calculate_store(goods, store) == [
        'Лампа - 5 шт, стоимость 800 руб'
    ]


def test_10_store_multiple_goods():
    goods = {'Лампа': '1', 'Стол': '2'}
    store = {
        '1': [{'quantity': 10, 'price': 42}],
        '2': [{'quantity': 5, 'price': 500}],
    }
    result = m10.calculate_store(goods, store)
    assert len(result) == 2
    assert 'Лампа - 10 шт, стоимость 420 руб' in result
    assert 'Стол - 5 шт, стоимость 2500 руб' in result