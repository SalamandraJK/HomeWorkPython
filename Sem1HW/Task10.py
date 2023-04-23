import random

N = int(input("Введите количество монет: "))
tails = 0
heads = 1
quantity_tails = 0
quantity_heads = 0

for _ in range(N):
    side = random.randint(0, 1)
    print(side, end=" ")
    if side == tails:
        quantity_tails += 1
    else: 
        if side == heads:
            quantity_heads += 1
print(f"\nСоотношение 0 и 1 ({quantity_tails} : {quantity_heads})")

if quantity_heads > quantity_tails:
    print(f"Ответ: {quantity_tails}")
    if quantity_heads == quantity_tails:
        print(f"Ответ: {N / 2}")
else:
    print(f"Ответ: {quantity_heads}")