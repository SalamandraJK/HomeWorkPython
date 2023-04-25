
n = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))

def pov(a,b):
    if a <= 0 or b < 0:
        return "Error"   
    if b == 0:
        return 1
    return pov(a * a, b - 1)

print(pov(n,k))