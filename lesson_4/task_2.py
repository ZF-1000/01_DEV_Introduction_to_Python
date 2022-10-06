"""
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

numb = int(input())
res = []
for i in range(2, numb):
    while numb % i == 0:
        res.append(i)
        numb /= i
print(res)

