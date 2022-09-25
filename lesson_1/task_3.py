"""
3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

x, y = [int(input()) for _ in range(2)]
print(f'x={x}; y={y} -> ', end='')
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x == 0 and y != 0:
    print('Точка находится на оси y')
elif y == 0 and x != 0:
    print('Точка находится на оси x')
elif x == 0 and y == 0:
    print('Точка находится на пересечении оси x и y')
