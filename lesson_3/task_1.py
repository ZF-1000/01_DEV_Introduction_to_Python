"""
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

import random

lst = [random.randint(-10, 10) for _ in range(10)]
odd_idx = list(range(1, len(lst), 2))
el_odd_idx = [lst[i] for i in odd_idx]
print(f'{lst} -> на нечётных позициях элементы {el_odd_idx}, ответ: {sum(el_odd_idx)}')
