# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai 
# (можно использовать псевдогенерацию). Последняя строка содержит число X.

import random

counts = 0
n = int(input("Задайте длинну массива: "))
x = int(input("Задайте искомое число: "))
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)

for i in range(n):
    if lst[i] == x:
        counts += 1
print(counts)