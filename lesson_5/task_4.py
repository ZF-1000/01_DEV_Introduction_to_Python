"""
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""
with open('test_5_4_inp.txt', encoding='utf-8') as inp, \
        open('test_5_4_out.txt', 'w', encoding='utf-8') as out:
    context = inp.readlines()

    for i in range(len(context)):
        res = []
        cnt = 0
        start = 0
        cont = context[i].strip()
        for j in range(len(cont)):
            if cont[start] == cont[j]:
                cnt += 1
            else:
                start = j
                # print(cnt, cont[j - 1], sep='', end='')
                res.append(f'{cnt}{cont[j - 1]}')
                cnt = 1
            if j == len(cont) - 1:
                # print(cnt, cont[j], sep='', end='')
                res.append(f'{cnt}{cont[j]}')
        # print()
        print(''.join(res), file=out)
