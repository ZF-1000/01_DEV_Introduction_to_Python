"""
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

numb_10 = int(input('Введите целое число: '))
print(numb_10, end='')
res = ''
while numb_10 // 2 >= 1:
    res += str(numb_10 % 2)
    numb_10 //= 2

res += str(numb_10)
print(f' -> {res[::-1]}')
