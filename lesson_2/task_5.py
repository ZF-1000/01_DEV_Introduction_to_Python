"""
5. Реализуйте алгоритм перемешивания списка.
"""

# Способ №1
import random

lst_1 = [1, 2, 3, '5', '7', '345', 'sdg', True, False]
print('Начальный список: ', lst_1, sep='\n')
random.shuffle(lst_1)
print(f'Перемешанный список: ', lst_1, sep='\n')


# Способ №2
print()
res = []
lst_2 = [1, 2, 3, '5', '7', '345', 'sdg', True, False]
print('Начальный список: ', lst_2, sep='\n')
while len(lst_2):
    idx = random.randint(0, len(lst_2) - 1)
    res.append(lst_2[idx])
    lst_2.remove(lst_2[idx])
print(f'Перемешанный список: ', res, sep='\n')