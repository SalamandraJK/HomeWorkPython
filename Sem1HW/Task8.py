# Задача №8. 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите кол-во долек N: "))
m = int(input("Введите кол-во долек M: "))
k = int(input("Введите кол-во долек K: "))

if (k % m == 0 or k % n == 0) and k < n * m - n:
    print('ok')
else:
    print('Nonono')