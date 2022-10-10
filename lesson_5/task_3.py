"""
3. Создайте программу для игры в ""Крестики-нолики"" с ботом.
"""

from random import randint
import time


def draw_board(brd):
    for i in range(len(brd)):
        if i in [3, 6]:
            print()
        print(brd[i], end=' ')


def first_step():
    print()
    flg = True
    while flg:
        try:
            n = int(input('Введите "1" если хотите ходить первым и "2" - вторым: '))
            if n == 1:
                return True
            elif n == 2:
                return False
        except:
            print('Некорректный ввод!')


def take_input(brd, flg):
    if flg:
        while 1:
            try:
                step = input('\nКуда поставим "X": ')
                if (1 <= int(step) <= 9) and (step not in steps):
                    steps.append(step)
                    break
                else:
                    print('Некорректный ввод!')
            except:
                print('Некорректный ввод!')
        brd = brd.replace(step, 'X')
        flg = False
    else:
        step = str(randint(1, 9))
        fl_step = True
        while fl_step:
            if step not in steps:
                print(f'\n{player_2} ставит "O": ', end='')
                time.sleep(1)
                print(step)
                steps.append(step)
                break
            else:
                step = str(randint(1, 9))
        brd = brd.replace(step, 'O')
        flg = True
    return brd, flg


def check_win(brd):
    if brd[0:3] == 'XXX' or \
            brd[3:6] == 'XXX' or \
            brd[6:] == 'XXX' or \
            brd[0::3] == 'XXX' or \
            brd[1::3] == 'XXX' or \
            brd[2::3] == 'XXX' or \
            brd[0::4] == 'XXX' or \
            brd[2:7:2] == 'XXX':
        print(f'\n\n{player_1} победил!')
        exit()
    elif brd[0:3] == 'OOO' or \
            brd[3:6] == 'OOO' or \
            brd[6:] == 'OOO' or \
            brd[0::3] == 'OOO' or \
            brd[1::3] == 'OOO' or \
            brd[2::3] == 'OOO' or \
            brd[0::4] == 'OOO' or \
            brd[2:7:2] == 'OOO':
        print(f'\n\n{player_2} победил!')
        exit()


player_1 = 'nik'
player_2 = 'bot'
board = '123456789'
draw_board(board)

flag = first_step()
steps = []

while 1:
    board, flag = take_input(board, flag)
    draw_board(board)
    check_win(board)
