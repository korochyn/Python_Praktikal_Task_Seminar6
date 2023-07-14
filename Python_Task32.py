# Урок 6. Повторение списков
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Сочиняем массив с числами
n = int(input('Введите количество элементов массива :'))
min = int(input('Введите нижнюю границу массива :')) # минимальная величина массива
max = int(input('Введите верхнюю границу массива :')) # максимальная величина массива
import random
list_num = list()
for i in range(0, n):
    list_num.append(random.randint(min, max))

print (f'Мы получили вот такой массив {list_num}')

# Вводим параметры поиска
num_min = int(input('Введите нижнюю границу заданного диапазона поиска :'))
num_max = int(input('Введите верхнюю границу заданного диапазона поиска :'))
if num_min > num_max:
    num_tmp = num_max 
    num_max = num_min
    num_min = num_tmp

list_index = list()
# Поиск
for i in range(0, n-1):
    if num_min <= list_num[i] <= num_max:
        list_index.append(i)
        print(i)
print(f'В заданноми диапазоне находятся числа с индексами {list_index}')  