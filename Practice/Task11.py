# Fib_Num_1 = 0
# Fib_Num_2 = 1
# Sum_Fib_Num = 0
# i = 0

# N = int(input("Введите число Фибоначчи: "))

# if N == 0:
#     print(f"Это {i}-e число Фибоначчи")  
# else:
#     i = 1
#     while Sum_Fib_Num != N:
#         Sum_Fib_Num = Fib_Num_1 + Fib_Num_2
#         Fib_Num_1 = Fib_Num_2
#         Fib_Num_2 = Sum_Fib_Num
#         i += 1
# print(f"Это {i}-e число Фибоначчи")


Fib_Num_1 = 0
Fib_Num_2 = 1
i = 1
N = int(input("Введите число Фибоначчи: "))

while Fib_Num_1 < N:
    Fib_Num_1, Fib_Num_2 = Fib_Num_2, Fib_Num_1 + Fib_Num_2
    i += 1
if Fib_Num_1 != N:
    print("Введено число не из ряда Фибоначчи")
else:
    print(f"Это {i}-e число Фибоначчи")