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

first_num = 1
second_num = 1

x = random.randint(1, 100)
y = random.randint(1, 100)
for first_num in range(x + 1):
    for second_num in range(y + 1):
        if (first_num == x + y) and (second_num == x * y):
            sum = x + y
            multi = x * y

print(f"Сумма двух чисел = {x + y}")
print(f"Произведение двух чисел = {x * y}")           
print(f"Загаданные числа {first_num} и {second_num}")
        