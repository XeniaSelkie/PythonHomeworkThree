#Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.

import random

a=[]
n = int(input("Введите число элементов в массиве: "))
for i in range(n):
    a.append(random.randint(1,10))
print(a)

x = int(input("Введите искомое число: "))

module = abs(x - max(a))        
for i in a:
    if abs(x - i) < module:
        module = abs(x - i)
        closest_number = i

print(f"Наиболее близкое к исходному число {closest_number}")        