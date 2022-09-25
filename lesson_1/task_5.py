"""
5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
print('Введите координаты точки А: ')
x_1, y_1 = [int(input()) for _ in range(2)]
print('Введите координаты точки B: ')
x_2, y_2 = [int(input()) for _ in range(2)]
AB = round(((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5, 2)
print(f'A ({x_1},{y_1}); B ({x_2},{y_2}) -> {AB}')
