# Задача №4. 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

NumCrane = int(input('Введите общее число сделанных журавликов, кратное 6: '))

if NumCrane % 6 == 0:
    PetiaNum = Seregja = NumCrane / 6
    KateNum = (Seregja + PetiaNum)*2
    print(f"Катя сделала: {KateNum}; Петя сделал: {PetiaNum}; Сережа сделал: {Seregja}")
else:
    print("Введено неверное число")