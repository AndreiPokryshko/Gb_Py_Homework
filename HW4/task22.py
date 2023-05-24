# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.#     1 2 3 4 5

import random
n = int(input("Введите кол-во элементов в 1-м множестве: "))
m = int(input("Введите кол-во элементов во 2-м множестве: "))



list_num1 = []
list_num2 = []
set_num = set()

count = 0
for item in range(n):
    list_num1.append(random.randint(1, 20))
for i in range(m):
    list_num2.append(random.randint(1, 20))
set_num=set(list_num1+list_num2)
print(f'lis1= {list_num1}')
print(f'lis2= {list_num2}')
print(f'set= {set_num} - {type(set_num)}')


