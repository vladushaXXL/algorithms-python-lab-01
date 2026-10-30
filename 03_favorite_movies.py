#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_movie_parts(movies_string):
    """Возвращает (первый, последний, второй, второй с конца) через срезы."""
    first = movies_string[0:10]
    last = movies_string[42:]
    second = movies_string[12:25]
    second_from_end = movies_string[35:40]
    return first, last, second, second_from_end


if __name__ == '__main__':
    my_favorite_movies = (
        'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    )
    for part in get_movie_parts(my_favorite_movies):
        print(part)