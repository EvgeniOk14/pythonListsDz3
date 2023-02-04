# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X


from random import*
n = int(input('введите размер массива n: '))
list1 = [randint(0, 11) for i in range(n)]
print(list1)
x = int(input('Введите число x: '))
min = 0
for element in list1:

    if x == element or x == element + 1 or x == element - 1: 
        min = element
print(min)


