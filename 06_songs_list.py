#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_songs_list(songs_list, song_names):
    """Суммарное время песен из списка списков."""
    total = 0.0
    for name, duration in songs_list:
        if name in song_names:
            total += duration
    return round(total, 3)


def sum_songs_dict(songs_dict, song_names):
    """Суммарное время песен из словаря."""
    total = sum(songs_dict[name] for name in song_names)
    return round(total, 3)


if __name__ == '__main__':
    violator_songs_list = [
        ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56], ['Halo', 4.9],
        ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83],
    ]
    violator_songs_dict = {
        'World in My Eyes': 4.76, 'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56, 'Halo': 4.30,
        'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68,
    }
    print('Три песни звучат', sum_songs_list(
        violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean']), 'минут')
    print('А другие три песни звучат', sum_songs_dict(
        violator_songs_dict,
        ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']), 'минут')