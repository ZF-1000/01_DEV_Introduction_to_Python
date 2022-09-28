"""
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""
import random

N = int(input('Введите число N: '))
lst = [random.randint(-N, N) for _ in range(N)]
print(f'Cписок из {N} элементов, заполненный числами из промежутка [-{N}, {N}]:', lst)

with open('test.txt', encoding='utf-8') as inp:
    context = inp.read()
    pos = (list(map(int, context.strip().split('\n'))))

res = 1
for i in pos:
    res *= lst[i]
print(f'Произведение элементов на позициях {pos}: ', res)