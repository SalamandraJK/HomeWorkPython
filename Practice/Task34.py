# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# listVinny = str(input("Введите строку через пробел: "))


# def point(string):
#     count = 0
#     for i in listVinny: 
#         if i == 'а':
#             count = count + 1
#         elif i == 'о':
#             count = count + 1
#         elif i == 'ы':
#             count = count + 1
#         elif i == 'и':
#             count = count + 1
#         elif i == 'э':
#             count = count + 1
#         elif i == 'я':
#             count = count + 1
#         elif i == 'ю':
#             count = count + 1
#         elif i == 'е':
#             count = count + 1
#         else:
#             return count

# # counter = listVinny.count('а, у, о, ы, и, э, я, ю, е')
# print(point(listVinny))


string_Vinny = str(input("Введите фразу: "))
string_Vinny = string_Vinny.split()

def check_rhyme(string):
    list = []
    for i in string:
        counts = 0
        for j in i:
            if j in 'аеёиоуыэюя':
                counts += 1
        list.append(counts)
    return len(list) == list.count(list[0])

if check_rhyme(string_Vinny):
    print('Парам пам-пам')
else:
    print('Пам парам')