"""
2. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

"""
Вариант с ботом. Если по жеребьёвке бот будет ходить первым, то он выиграет
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


def get_sweet_bot(name, score):
    sweet = score % 29      # бот с "интеллектом"
    if sweet != 0:
        print(f'Ходит {name}: {sweet}')
        return sweet
    else:
        sweet = randint(1, 28)  # бот без "интеллекта"
        print(f'Ходит {name}: {sweet}')
        return sweet


player_1 = input(f'Введите имя игрока: ')
player_2 = 'Bot'

flag = randint(0, 1)
# flag = 1 # чтобы первый ходил игрок, а не бот
print('-------- Первый ходит:', f'{player_1} --------' if flag else f'{player_2} --------')
print('За один ход можно забрать не более чем 28 конфет')
score = 2021
while score > 28:
    print(f'Конфет осталось: {score}')
    if flag:
        score -= get_sweet(player_1)
        flag = False
    else:
        score -= get_sweet_bot(player_2, score)
        flag = True

print(f'Конфет осталось: {score}')
print(f'Выиграл:', player_1 if flag else player_2)

