# №27. 
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.

# Input: 
# She sells sea shells on the sea shore 
# The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore 
# I'm sure that the shells are sea shore shells

s = ('She sells sea shells on the sea shore The shells that she sells are sea shells I am sure So if she sells sea shells on the sea shore I am sure that the shells are sea shore shells').lower()
print(len(set(s)))
# counts = {}
# i = 0
# for j in s.split():
#     if j not in counts:
#         counts[j] = 1
#         i += 1
#     else:
#         counts[j] += 1

# print(counts)
# print(i)