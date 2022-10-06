"""
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random

k = int(input())
lst_k = [random.randint(0, 100) for _ in range(k + 1)]
res = []
for i in range(len(lst_k)):
    if lst_k[i] == 0:
        continue
    elif k - i == 0:
        res.append(f'{lst_k[i]}')
    elif k - i == 1:
        res.append(f'{lst_k[i]}*x')
    else:
        res.append(f'{lst_k[i]}*x^{k - i}')
print(f'k = {k} -> ', ' + '.join(res), ' = 0', sep='', file=open('test.txt', 'a'))
