# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Если число x не наайдено, то выводит. самый близкий по величине элемент к заданному числу X.
#  *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
n = int(input("Введите кол-во элементов в массиве: "))

list_num = []
count = 0
for item in range(n):
    list_num.append(random.randint(1, 20))
# list_num=[i for i in random.randint(1,100)]
x = int(input(f"Какое число из списка от 1 до 9 считать: "))
print(list_num)
print(x)
for i in range(len(list_num)):
    if list_num[i] == x:  # если число найдено то считает кол-во совпадений
        count += 1
if count > 0:# если число не найдено то искать ближайшее
    print("->", count)
else:
    dif= abs(list_num[0]-x)
    blizh = 0
    for i in range(len(list_num)):
        if dif > abs(list_num[i]-x):
            dif = abs(list_num[i]-x)
            blizh = list_num[i]
    print("ближайшее ->", blizh)
