#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.

import random

a=[]
n = int(input("Введите число элементов в массиве: "))
for i in range(n):
    a.append(random.randint(1,10))
print(a)

x = int(input("Введите искомое число: "))

list_x = []
for i in a:
    if i == x:
        list_x.append(i)
print(len(list_x))


