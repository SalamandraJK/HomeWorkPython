# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input("Задайте длинну массива: "))
max_1 = int(input("Задайте максимальное значение массива: "))
min_1 = int(input("Задайте минимальное значение массива: "))
max_num = int(input("Задайте максимальное значение поиска: "))
min_num = int(input("Задайте минимальное значение поиска: "))
lst_1 = [random.randint(min_1, max_1) for i in range(n)]
print(lst_1)
lst_2 = []
for i in range(n):
    if min_num < lst_1[i] < max_num:
        lst_2.append(i)

print(lst_2)