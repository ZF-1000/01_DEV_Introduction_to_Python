"""
2. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""
from random import randint


def get_sweet(name):
    print(f'Ходит {name}: ', end='')
    try:
        sweet = int(input())
    except:
        print('Некорректный ввод!')
    while not 0 < sweet < 29:
        try:
            sweet = int(input('Введите число от 1 до 28: '))
        except:
            print('Некорректный ввод!')
    return sweet


player_1, player_2 = [input(f'Введите имя игрока №{_}: ') for _ in range(1, 3)]

flag = randint(0, 1)
print('-------- Первый ходит:', f'{player_1} --------' if flag else f'{player_2} --------')
print('За один ход можно забрать не более чем 28 конфет')
score = 2021
while score > 28:
    print(f'Конфет осталось: {score}')
    if flag:
        score -= get_sweet(player_1)
        flag = False
    else:
        score -= get_sweet(player_2)
        flag = True

print(f'Конфет осталось: {score}')
print(f'Выиграл:', player_1 if flag else player_2)

