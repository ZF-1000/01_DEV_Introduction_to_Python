"""
2. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

import random

lst = [random.randint(-10, 10) for _ in range(10)]
lst_num = list(enumerate(lst))
lst_el_odd_idx = list(filter(lambda x: x[0] % 2 != 0, lst_num))
el_odd_idx = list(zip(*lst_el_odd_idx))[1]
print(f'{lst} -> на нечётных позициях элементы {el_odd_idx}, ответ: {sum(el_odd_idx)}')