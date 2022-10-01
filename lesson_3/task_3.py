"""
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import random

lst = [round(random.uniform(17, 20), 2) for _ in range(5)]
str_1 = list(map(str, lst))
fract_part = list(map(int, [x.split('.')[1] for x in str_1]))
print(f'{lst} => {max(fract_part)} - {min(fract_part)} = {max(fract_part) - min(fract_part)}')
