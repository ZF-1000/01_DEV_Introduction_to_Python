"""
3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
"""

N = int(input('Введите число N: '))


def func(n):
    return (1 + 1 / n) ** n


res = 0
for i in range(1, N + 1):
    res += func(i)
    print(f'{i}: {func(i)}')
print(f'Сумма чисел: {round(res, 5)}')

