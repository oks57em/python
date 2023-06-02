# написать программу для нахождения максимального
# числа ягод,которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входной
# файле грядки.

from random import randint
list_1 = list(randint(1,5)for i in range(int(input("Ввести количество кустов:"))))
print(list_1)
a = int(input("Ввести номер куста:"))
res = 0
if a == 1:
        res = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
        res = list_1[-2] + list_1[-1] + list_1[0]
else:
        res = list_1[a-1] + list_1[a-2] + list_1[a]
print(res)


         
