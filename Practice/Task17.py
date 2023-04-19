# Задача, на нахождение колличества ислючительных значений в сгенерированном списке(массиве)

import random

counts = 0
list_1 = []
n = int(input("Задайте длинну массива "))
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)

for j in lst:
    if not j in list_1:
        list_1.append(j)

print(len(list_1)) 
