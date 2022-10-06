"""
5. Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""

with open('test_5_1.txt', encoding='utf-8') as inp_1, \
        open('test_5_2.txt', encoding='utf-8') as inp_2, \
        open('test_5_out.txt', 'w', encoding='utf-8') as out:
    context_1 = inp_1.read()
    context_2 = inp_2.read()
    lst_cont_1 = context_1.strip()
    lst_cont_2 = context_2.strip()
    print(lst_cont_1)
    print(lst_cont_2)
    lst_1 = lst_cont_1.split(' ')[:-2:2]
    lst_2 = lst_cont_2.split(' ')[:-2:2]

    res = ''
    for i in range(len(lst_1)):
        res += str(int(lst_1[i].split('*x')[0]) + int(lst_2[i].split('*x')[0]))
        if i != len(lst_1) - 1:
            res += f'*x' + lst_1[i].split('*x')[1] + ' + '
        else:
            res += ' = 0'
    print(res)
    out.write(res)
