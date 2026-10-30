#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# Динамический импорт модулей с числовыми именами
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


def task_distance():
    print("\n[00] Расстояния между городами")
    sites = {'Moscow': (550, 370), 'London': (510, 510), 'Paris': (480, 480)}
    distances = m00.get_distances(sites)
    for city, others in distances.items():
        for target, dist in others.items():
            print(f"  {city} -> {target}: {dist}")


def task_circle():
    print("\n[01] Площадь круга и точки")
    print(f"  Площадь (R=42): {m01.circle_area(42)}")
    print(f"  (23, 34) внутри: {m01.is_point_in_circle((23, 34), 42)}")
    print(f"  (30, 30) внутри: {m01.is_point_in_circle((30, 30), 42)}")


def task_expression():
    print("\n[02] Число 25 из 1 2 3 4 5")
    print(f"  Результат: {m02.make_25()}")


def task_movies():
    print("\n[03] Срезы названий фильмов")
    s = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    first, last, second, second_from_end = m03.get_movie_parts(s)
    print(f"  Первый: {first}")
    print(f"  Последний: {last}")
    print(f"  Второй: {second}")
    print(f"  Второй с конца: {second_from_end}")


def task_family():
    print("\n[04] Рост членов семьи")
    heights = [
        ['мама', 165], ['папа', 180], ['брат', 175],
        ['сестра', 160], ['бабушка', 155], ['дедушка', 170],
    ]
    print(f"  Рост отца: {m04.father_height(heights)} см")
    print(f"  Общий рост: {m04.total_family_height(heights)} см")


def task_zoo():
    print("\n[05] Животные в зоопарке")
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    updated, lion_cell, lark_cell = m05.process_zoo(zoo, birds)
    print(f"  Итог: {updated}")
    print(f"  Лев в клетке №{lion_cell}")
    print(f"  Жаворонок в клетке №{lark_cell}")


def task_songs():
    print("\n[06] Длительность песен Depeche Mode")
    songs_l = [
        ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56], ['Halo', 4.9],
        ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83],
    ]
    songs_d = {
        'World in My Eyes': 4.76, 'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56, 'Halo': 4.30,
        'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68,
    }
    t1 = m06.sum_songs_list(songs_l, ['Halo', 'Enjoy the Silence', 'Clean'])
    t2 = m06.sum_songs_dict(
        songs_d,
        ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'],
    )
    print(f"  Три песни (список): {t1} минут")
    print(f"  Три песни (словарь): {t2} минут")


def task_secret():
    print("\n[07] Расшифровка секретного сообщения")
    secret = [
        'каквтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    print(f"  \"{m07.decrypt_message(secret)}\"")


def task_garden():
    print("\n[08] Цветы сада и луга")
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка',
              'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер',
              'мак', 'одуванчик', 'ромашка')
    all_f, both, only_g, only_m = m08.garden_operations(garden, meadow)
    print(f"  Все виды: {all_f}")
    print(f"  И там, и там: {both}")
    print(f"  Только в саду: {only_g}")
    print(f"  Только на лугу: {only_m}")


def task_shopping():
    print("\n[09] Минимальные цены в магазинах")
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99},
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99},
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99},
        ],
    }
    sweets = m09.find_best_prices(shops)
    for product, offers in sweets.items():
        print(f"  {product}:")
        for o in offers:
            print(f"    {o['shop']} — {o['price']} руб")


def task_store():
    print("\n[10] Складской учёт")
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
    for line in m10.calculate_store(goods, store):
        print(f"  {line}")


TASKS = {
    '0': task_distance,
    '1': task_circle,
    '2': task_expression,
    '3': task_movies,
    '4': task_family,
    '5': task_zoo,
    '6': task_songs,
    '7': task_secret,
    '8': task_garden,
    '9': task_shopping,
    '10': task_store,
}


def run_all():
    print("  ЛАБОРАТОРНАЯ РАБОТА №1 — ВСЕ ЗАДАНИЯ")
    for key in sorted(TASKS, key=int):
        TASKS[key]()
    print("\nГотово.")


def menu():
    print("\n")
    print("  МЕНЮ ЗАДАНИЙ")
    for key in sorted(TASKS, key=int):
        print(f"  [{key:>2}] {TASKS[key].__name__}")
    print("  [all] Все подряд")
    print("  [ q ] Выход")


def main():
    while True:
        menu()
        choice = input("Ваш выбор: ").strip().lower()
        if choice in ('q', 'quit', 'exit', 'й'):
            break
        elif choice == 'all':
            run_all()
        elif choice in TASKS:
            TASKS[choice]()
        else:
            print("[!] Введите 0–10, 'all' или 'q'")
        input("\nEnter — продолжить...")


if __name__ == '__main__':
    main()