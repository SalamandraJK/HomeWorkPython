# №23. 
# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

import random

counts = 0
n = int(input("Задайте длинну массива: "))
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)
j = 1
while j < n:
    if lst[j - 1] < lst[j]:
        counts += 1
    j += 1
print(counts)


counts = 0
for i in range(n - 1):
    if lst[i] < lst[i + 1]:
        counts += 1
print(counts)