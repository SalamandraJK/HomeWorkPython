
#Метод вывода уникальных значений из *списка словарей*

slovar_1 =[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
 {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

dict = set()
for i in slovar_1:
    dict.add(*i.values())

print(dict) 