num = int(input('Введите число: '))
i = 0
result = 0
while result < num + 1:
    result = 2 ** i
    print(result)
    i += 1