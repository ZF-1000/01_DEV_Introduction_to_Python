"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0.56 -> 11
"""

numb = float(input('Введите вещественное число: '))
lst = list(str(numb).replace('.', ''))
print(sum(map(int, lst)))
