# Fib_Num_1 = 0
# Fib_Num_2 = 1
# Sum_Fib_Num = 0
# i = 0

# n = int(input("Введите число Фибоначчи: "))

# if n == 0:
#     print(f"Это {i}-e число Фибоначчи")  
# else:
#     i = 1
#     while Sum_Fib_Num != n:
#         Sum_Fib_Num = Fib_Num_1 + Fib_Num_2
#         Fib_Num_1 = Fib_Num_2
#         Fib_Num_2 = Sum_Fib_Num
#         i += 1
# print(f"Это {i}-e число Фибоначчи")


Fib_Num_1 = 0
Fib_Num_2 = 1
i = 1
n = int(input("Введите число Фибоначчи: "))

while Fib_Num_1 < n:
    Fib_Num_1, Fib_Num_2 = Fib_Num_2, Fib_Num_1 + Fib_Num_2
    i += 1
if Fib_Num_1 != n:
    print("Введено число не из ряда Фибоначчи")
else:
    print(f"Это {i}-e число Фибоначчи")

def fibNum(num, fstNum, secNum, currNum):
    if num < 1: return "error"
    elif num == 1: return 0
    elif num == 2: return 1
    else:
        nextNum = fstNum + secNum
        currNum += 1
        if currNum == num:
            return nextNum
        return fibNum(num,
                      fstNum=secNum,
                      secNum=nextNum,
                      currNum=currNum)


print(fibNum(7, 0, 1, 2))