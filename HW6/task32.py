# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
min_ = int(input("Минимальная граница:"))
max_ = int(input("Макс граница:"))
list_ = list(random.randint(1, 100) for i in range(20))
print(list_)
list_indx = []
for i in range(len(list_)):
    if min_ <= list_[i] <= max_:
        list_indx.append(i)
print(list_indx)
