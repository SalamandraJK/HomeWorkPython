import random


n = int(input("Задайте длинну первого массива: "))
max_num1 = int(input("Задайте максимальное значение первого массива: "))
lst_1 = {random.randint(0, max_num1) for i in range(n)}

m = int(input("Задайте длинну второго массива: "))
max_num2 = int(input("Задайте максимальное значение второго массива: "))
lst_2 = {random.randint(0, max_num2) for i in range(m)}

print(lst_1)
print(lst_2)

i = lst_2.intersection(lst_1)   # Будет содержать общие элементы из двух списков
j = sorted(i)
j.sort()
print(j)