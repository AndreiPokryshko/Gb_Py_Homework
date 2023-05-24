# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def my_pow(n, m):
    if m == 1:
        return n
    # if m != 1:
    return n * my_pow(n, m - 1)

n = int(input("Введите число А: "))
m = int(input("Введите число В: "))
print (type(n))
print (type(m))
print(my_pow(n, m))
