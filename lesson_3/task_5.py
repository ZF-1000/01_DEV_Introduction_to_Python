"""
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""


def negafib(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    else:
        return negafib(n + 2) - negafib(n + 1)


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


k = int(input('Введите k: '))
nefib_lst = [negafib(i) for i in range(-1, -k - 1, -1)]
fib_lst = [fib(i) for i in range(1, k + 1)]
print(f'Для k = {k} список будет выглядеть так:')
print(nefib_lst[::-1] + [0, ] + fib_lst)
