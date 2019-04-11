# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fibo_list = [1, 1]
    i = 1
    while i != m:
        fibo_list.append((fibo_list[i-1] + fibo_list[i]))
        i += 1
    return fibo_list[n: m + 1]


# проверка
print(fibonacci(0, 5))
print(fibonacci(5, 14))
print()
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):  # итерация общая
        for j in range(len(origin_list) - 1 - i):  # ищем новый пузырь и поднимаем.
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]  # исп. кортеж, меняем местами
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print()
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(required, array):
    my_array = []
    for i in range(len(array)):
        if array[i] == required:
            my_array.append(array[i])
    return my_array


you_array = ['Воздушный рис', 'мед', 'варенье', 'зефир', 'мед', 'мусс', 'мед', 'пастила', 'сухое печенье']
print(my_filter('мед', you_array))
print()
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogramm(a1, a2, a3, a4):
    if abs(a1[0] - a4[0]) == abs(a2[0] - a3[0]) and abs(a1[1] - a2[1]) == abs(a3[1] - a4[1]):
        return 'Параллелограмм'
    return 'Не параллелограм'


print(parallelogramm((6, 1), (1, 3), (1, 1), (6, 3)))
print(parallelogramm((1, 1), (1, 3), (6, 1), (6, 3)))
