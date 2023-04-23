import random

n = int(input("Введите число: "))

list_cust = []
for i in range(n):
    list_cust.append(random.randint(1, n*2))

temp_val = 0
print(list_cust)
step = 3
if len(list_cust) > step:
    val = temp_val = sum(list_cust[:step])

    for i in range(n-1):
        j = (i + step) % n
        val = val - list_cust[i] + list_cust[j]

        if val > temp_val:
            temp_val = val

elif len(list_cust) == step:
    temp_val = sum(list_cust[:step])

print(temp_val)