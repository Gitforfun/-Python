# Все задачи текущего блока решите с помощью генераторов списков!
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


def square_items(orig_list):
    return [digit**2 for digit in orig_list]


print([1, 2, 4, 0], " --> ", square_items([1, 2, 4, 0]))
print()

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_fruits = ["яблоко", "банан", "киви", "ананас", "груша", "абрикос"]
second_fruits = ["яблоко", "виноград", "киви", "арбуз", "дыня", "персик"]
third_fruits = [fruit for fruit in first_fruits if fruit in second_fruits]

print(first_fruits, '\n', second_fruits, '\n', third_fruits)
print()

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random


def conditions_list(origin_list):
    return [item for item in origin_list if item % 3 == 0 and item > 0 and item % 4 != 0]


print(conditions_list([random.randint(-30, 30) for i in range(30)]))
