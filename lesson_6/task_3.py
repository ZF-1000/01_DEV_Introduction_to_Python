"""
3. Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
import random

lst_in = [random.randint(0, 5) for _ in range(10)]
print(f'Исходная последовательность: {lst_in}')
print(f'Список неповторяющихся элементов исходной последовательности: ', end='')
print(list(filter(lambda x: lst_in.count(x) == 1, lst_in)))
