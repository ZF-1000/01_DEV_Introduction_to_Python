"""
3. Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
import random

lst_in = [random.randint(0, 5) for _ in range(10)]
print(f'Исходная последовательность: {lst_in}')
res = []
for x in lst_in:
    if lst_in.count(x) == 1:
        res.append(x)
print(f'Список неповторяющихся элементов исходной последовательности: ', res if len(res) else 'уникальных элементов нет')