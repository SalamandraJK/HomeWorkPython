import random
# x = random.randint(1, 10)
# y = random.randint(1, 10)
# sum = 0
# multi = 0
# first_num = 1
# second_num = 1
# print(f"Сумма двух чисел = {sum == x + y}")
# print(f"Произведение двух чисел = {multi == x * y}")

# for first_num in range(x):
#     for second_num in range(y):
#         if first_num == x + y and second_num == x * y:
#             sum == x + y
#             multi == x * y

# print(f"Загаданные числа {first_num} и {second_num}")

# x = random.randint(1, 100)
# y = random.randint(1, 100)
x = int(input("Загадайте сумму: "))
y = int(input("Загадайте произведение Y: "))
# sum = x + y
# multi = x * y

for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:      
            print(f"Загаданные числа {i} и {j}")
            break
    else:
        continue
    break
else:
    print("Решение не найдено")


        