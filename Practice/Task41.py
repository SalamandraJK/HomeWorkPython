# Задача №41.
# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 

import random
count = 0
n = int(input("Задайте длинну массива: "))
lst_1 = [random.randint(0, 10) for i in range(n)]
print (lst_1)
for i in range(n - 2):
    if lst_1[i] < lst_1[i + 1] > lst_1[i + 2]:
        count += 1
print(count)
