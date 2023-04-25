def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Введите число: "))
list_1 = []
for i in range(1, n):
    list_1.append(fib(i))
print(list_1)