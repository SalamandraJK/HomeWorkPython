
n = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))

def sum_num(a, b):
    if a < 0 or b < 0:
        return "Error"
    if a == 0 or b == 0:
        return a + b
    return sum_num(a + 1, b - 1)

print(sum_num(n, k))