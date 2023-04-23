import random

counts = 0
n = int(input("Задайте длинну массива: "))
k = int(input("Задайте сдвиг массива: "))
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)

# for (k) in lst:                     
#     lst.append(k)
#     print(lst)

for _ in range(k):
    lst.insert(0, lst.pop())

print(lst)