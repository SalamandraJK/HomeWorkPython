# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения

# print_operation_table(lambda x, y: x * y)

# column  = int(input("Введите количество столбцов: "))

# for i in range(1, column):
#     for j in range(1, column):
#         print("%4d" % (i * j), end="")
#     print()

def print_operation_table(operation,
    num_r = int(input("Кол-во столбцов: ")),
    num_c = int(input("Кол-во строк: "))):
    a = [[operation(i, j) 
        for j in range(1, num_c + 1)] 
        for i in range(1, num_r + 1)]
    
    for i in a:
        print(*[f"{x: 4d}" for x in i])


print_operation_table(lambda x, y: x * y)